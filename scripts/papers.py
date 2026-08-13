#!/usr/bin/env python3
"""Fail-closed paper asset preflight, synchronization, and import CLI."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile
from typing import Any, Iterable, TextIO
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


SCHEMA_VERSION = 1
CHUNK_SIZE = 1024 * 1024
MAX_DOWNLOAD_BYTES = 512 * 1024 * 1024
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REDISTRIBUTION_STATUSES = {
    "UNKNOWN",
    "PUBLIC_DOMAIN",
    "REDISTRIBUTION_ALLOWED",
    "RESTRICTED",
}
ACQUISITION_STATUSES = {
    "UNKNOWN",
    "DIRECT_PUBLIC",
    "MANUAL_ONLY",
}
OPERATIONAL_FIELDS = {
    "id",
    "aliases",
    "title",
    "authors",
    "year",
    "venue",
    "doi",
    "needs_metadata",
    "required",
    "acquisition_status",
    "source_url",
    "download_url",
    "redistribution_status",
    "license",
    "local_path",
    "sha256",
    "parse_status",
    "parse_warnings",
    "same_work",
    "cited_by_reports",
}


class CatalogLoadError(RuntimeError):
    """Raised when the catalog cannot be loaded safely."""


class PaperOperationError(RuntimeError):
    """Raised when an individual paper operation cannot complete safely."""


class StrictHTTPSRedirectHandler(HTTPRedirectHandler):
    """Reject redirects before any non-HTTPS or credentialed target is fetched."""

    def redirect_request(
        self,
        request: Request,
        file_pointer: Any,
        code: int,
        message: str,
        headers: Any,
        new_url: str,
    ) -> Request | None:
        _validate_download_url(new_url)
        return super().redirect_request(
            request, file_pointer, code, message, headers, new_url
        )


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return {}
    if value == "null":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.startswith(('"', "[", "{")):
        return json.loads(value)
    if value.startswith("*"):
        return value
    return value


def _load_restricted_yaml(text: str) -> dict[str, Any]:
    """Load the catalog subset with stdlib only.

    This parser intentionally accepts only the flat, machine-operational fields in
    this repository's catalog. If the catalog grows beyond that subset, callers
    fall back to PyYAML or receive an explicit dependency error.
    """

    schema_match = re.search(r"^schema_version:\s*(\d+)\s*$", text, re.MULTILINE)
    count_match = re.search(r"^paper_count:\s*(\d+)\s*$", text, re.MULTILINE)
    if not schema_match or not count_match or "\npapers:\n" not in text:
        raise CatalogLoadError("catalog is outside the built-in restricted YAML format")

    papers: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    in_papers = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line == "papers:":
            in_papers = True
            continue
        if not in_papers:
            continue
        id_match = re.match(r'^  - id:\s*(.+)\s*$', line)
        if id_match:
            if current is not None:
                papers.append(current)
            current = {"id": _parse_scalar(id_match.group(1))}
            continue
        if current is None:
            continue
        field_match = re.match(r"^    ([a-z][a-z0-9_]*):(?:\s*(.*))?$", line)
        if not field_match:
            continue
        key, raw_value = field_match.group(1), field_match.group(2) or ""
        if key not in OPERATIONAL_FIELDS:
            continue
        try:
            current[key] = _parse_scalar(raw_value)
        except (ValueError, json.JSONDecodeError) as exc:
            raise CatalogLoadError(
                f"unsupported scalar for {key!r} at line {line_number}: {exc}"
            ) from exc
    if current is not None:
        papers.append(current)
    if not papers:
        raise CatalogLoadError("catalog contains no paper records")

    minimum = {
        "id",
        "title",
        "doi",
        "required",
        "acquisition_status",
        "source_url",
        "download_url",
        "redistribution_status",
        "local_path",
        "sha256",
    }
    for paper in papers:
        missing = minimum - paper.keys()
        if missing:
            raise CatalogLoadError(
                f"built-in parser cannot recover {paper.get('id', '<unknown>')}: "
                f"missing {', '.join(sorted(missing))}"
            )
    return {
        "schema_version": int(schema_match.group(1)),
        "paper_count": int(count_match.group(1)),
        "papers": papers,
    }


def load_catalog(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CatalogLoadError(f"cannot read catalog {path}: {exc}") from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        try:
            return _load_restricted_yaml(text)
        except CatalogLoadError as restricted_error:
            try:
                import yaml  # type: ignore[import-not-found]
            except ModuleNotFoundError as exc:
                raise CatalogLoadError(
                    "catalog uses YAML outside the built-in supported subset and PyYAML "
                    "is not installed. Install it with `python3 -m pip install PyYAML`, "
                    f"then retry. Built-in parser detail: {restricted_error}"
                ) from exc
            try:
                data = yaml.safe_load(text)
            except Exception as exc:  # PyYAML exposes several parser exception types.
                raise CatalogLoadError(f"invalid YAML in {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise CatalogLoadError("catalog root must be a mapping")
    return data


def _url_error(value: Any, *, download: bool) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        return "must be null or a non-empty URL string"
    parsed = urlsplit(value)
    if parsed.scheme not in ({"https"} if download else {"http", "https"}):
        return "download_url must use HTTPS" if download else "must use HTTP or HTTPS"
    if not parsed.netloc:
        return "must include a network host"
    if parsed.username is not None or parsed.password is not None:
        return "must not embed login credentials"
    return None


def validate_schema(data: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION}; got {data.get('schema_version')!r}"
        )
    papers = data.get("papers")
    if not isinstance(papers, list):
        return errors + ["papers must be a list"]
    if data.get("paper_count") != len(papers):
        errors.append(
            f"paper_count={data.get('paper_count')!r} does not match records={len(papers)}"
        )

    seen_ids: dict[str, int] = {}
    seen_paths: dict[str, str] = {}
    root_resolved = root.resolve()
    required_fields = {
        "id",
        "title",
        "doi",
        "required",
        "source_url",
        "download_url",
        "redistribution_status",
        "local_path",
        "sha256",
    }
    for index, paper in enumerate(papers):
        label = f"papers[{index}]"
        if not isinstance(paper, dict):
            errors.append(f"{label} must be a mapping")
            continue
        paper_id = paper.get("id")
        if isinstance(paper_id, str) and paper_id:
            label = paper_id
            if paper_id in seen_ids:
                errors.append(f"{label}: duplicate id (first at index {seen_ids[paper_id]})")
            else:
                seen_ids[paper_id] = index
        else:
            errors.append(f"{label}: id must be a non-empty string")
        missing = sorted(required_fields - paper.keys())
        if missing:
            errors.append(f"{label}: missing fields {', '.join(missing)}")
            continue
        if not isinstance(paper.get("title"), str) or not paper["title"]:
            errors.append(f"{label}: title must be a non-empty string")
        if paper.get("doi") is not None and not isinstance(paper["doi"], str):
            errors.append(f"{label}: doi must be null or a string")
        if not isinstance(paper.get("required"), bool):
            errors.append(f"{label}: required must be boolean")
        status = paper.get("redistribution_status")
        if status not in REDISTRIBUTION_STATUSES:
            errors.append(
                f"{label}: redistribution_status={status!r} is not one of "
                f"{', '.join(sorted(REDISTRIBUTION_STATUSES))}"
            )
        acquisition_status = paper.get("acquisition_status")
        if acquisition_status not in ACQUISITION_STATUSES:
            errors.append(
                f"{label}: acquisition_status={acquisition_status!r} is not one of "
                f"{', '.join(sorted(ACQUISITION_STATUSES))}"
            )
        for key, download in (("source_url", False), ("download_url", True)):
            detail = _url_error(paper.get(key), download=download)
            if detail:
                errors.append(f"{label}: {key} {detail}")
        sha256 = paper.get("sha256")
        if not isinstance(sha256, str) or not SHA256_RE.fullmatch(sha256):
            errors.append(f"{label}: sha256 must be 64 lowercase hexadecimal characters")
        local_path = paper.get("local_path")
        if not isinstance(local_path, str) or not local_path:
            errors.append(f"{label}: local_path must be a non-empty string")
            continue
        posix_path = PurePosixPath(local_path)
        if posix_path.is_absolute() or ".." in posix_path.parts:
            errors.append(f"{label}: local_path must be a safe repository-relative path")
            continue
        if not posix_path.parts or posix_path.parts[0] != "papers":
            errors.append(f"{label}: local_path must be inside papers/")
        if local_path in seen_paths:
            errors.append(
                f"{label}: duplicate local_path also used by {seen_paths[local_path]}"
            )
        else:
            seen_paths[local_path] = str(paper_id)
        target = (root / Path(*posix_path.parts)).resolve(strict=False)
        try:
            target.relative_to(root_resolved)
        except ValueError:
            errors.append(f"{label}: local_path resolves outside the repository")
    return errors


def _target_path(root: Path, paper: dict[str, Any]) -> Path:
    return root / Path(*PurePosixPath(paper["local_path"]).parts)


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_file(path: Path, expected_sha256: str) -> tuple[str, str | None]:
    if not path.exists():
        return "MISSING", None
    if not path.is_file():
        return "NOT_A_FILE", None
    try:
        with path.open("rb") as stream:
            magic = stream.read(5)
        actual_sha256 = _hash_file(path)
    except OSError as exc:
        return "UNREADABLE", str(exc)
    if magic != b"%PDF-":
        return "INVALID_PDF_MAGIC", actual_sha256
    if actual_sha256 != expected_sha256:
        return "HASH_MISMATCH", actual_sha256
    return "OK", actual_sha256


def _ref(paper: dict[str, Any]) -> str:
    return (
        f"id={paper.get('id')} doi={paper.get('doi') or 'NONE'} "
        f"source_url={paper.get('source_url') or 'NONE'} "
        f"download_url={paper.get('download_url') or 'NONE'} "
        f"target={paper.get('local_path')}"
    )


def _manual_action(paper: dict[str, Any], state: str = "MISSING") -> str:
    if state != "MISSING":
        return (
            "move the unexpected target aside for provenance review, obtain a verified PDF, "
            f"then run `scripts/papers import {paper.get('id')} FILE`"
        )
    return (
        "obtain the PDF lawfully, then run "
        f"`scripts/papers import {paper.get('id')} FILE`"
    )


def _schema_or_report(
    data: dict[str, Any], root: Path, err: TextIO
) -> list[dict[str, Any]] | None:
    errors = validate_schema(data, root)
    if errors:
        for detail in errors:
            print(f"[SCHEMA_ERROR] {detail}", file=err)
        print(f"schema validation failed: {len(errors)} error(s)", file=err)
        return None
    return data["papers"]


def run_doctor(data: dict[str, Any], root: Path, out: TextIO, err: TextIO) -> int:
    papers = _schema_or_report(data, root, err)
    if papers is None:
        return 1
    issues = 0
    for paper in papers:
        state, detail = inspect_file(_target_path(root, paper), paper["sha256"])
        if state == "OK":
            continue
        if state == "MISSING" and not paper["required"]:
            continue
        issues += 1
        suffix = f" actual={detail}" if detail else ""
        print(
            f"[{state}] {_ref(paper)}{suffix} "
            f'manual_action="{_manual_action(paper, state)}"',
            file=err,
        )
    if issues:
        print(
            f"papers doctor: FAIL required_or_invalid={issues} checked={len(papers)}",
            file=err,
        )
        return 1
    print(f"papers doctor: OK checked={len(papers)}", file=out)
    return 0


def run_catalog_check(
    data: dict[str, Any], root: Path, checksum_manifest: Path, out: TextIO, err: TextIO
) -> int:
    """Validate the public paper contract without requiring local PDF files."""

    papers = _schema_or_report(data, root, err)
    if papers is None:
        return 1
    manifest_records: dict[str, str] = {}
    manifest_errors: list[str] = []
    try:
        lines = checksum_manifest.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"[CHECKSUM_MANIFEST_ERROR] cannot read {checksum_manifest}: {exc}", file=err)
        return 1
    for line_number, line in enumerate(lines, start=1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            manifest_errors.append(f"line {line_number}: invalid checksum record")
            continue
        digest, relative_path = match.groups()
        if relative_path in manifest_records:
            manifest_errors.append(f"line {line_number}: duplicate path {relative_path}")
            continue
        manifest_records[relative_path] = digest

    catalog_records = {paper["local_path"]: paper["sha256"] for paper in papers}
    for path in sorted(catalog_records.keys() - manifest_records.keys()):
        manifest_errors.append(f"missing manifest path {path}")
    for path in sorted(manifest_records.keys() - catalog_records.keys()):
        manifest_errors.append(f"unexpected manifest path {path}")
    for path in sorted(catalog_records.keys() & manifest_records.keys()):
        if catalog_records[path] != manifest_records[path]:
            manifest_errors.append(f"checksum differs for {path}")

    if manifest_errors:
        for detail in manifest_errors:
            print(f"[CHECKSUM_MANIFEST_ERROR] {detail}", file=err)
        print(
            f"papers catalog-check: FAIL errors={len(manifest_errors)} checked={len(papers)}",
            file=err,
        )
        return 1
    print(f"papers catalog-check: OK checked={len(papers)}", file=out)
    return 0


def _validate_download_url(url: str) -> None:
    detail = _url_error(url, download=True)
    if detail:
        raise PaperOperationError(detail)


def _atomic_commit(temp_path: Path, target: Path, expected_sha256: str) -> str:
    state, detail = inspect_file(temp_path, expected_sha256)
    if state != "OK":
        raise PaperOperationError(
            f"temporary file validation failed: state={state} actual={detail or 'NONE'}"
        )
    os.chmod(temp_path, 0o644)
    try:
        os.link(temp_path, target)
    except FileExistsError:
        existing_state, existing_detail = inspect_file(target, expected_sha256)
        if existing_state == "OK":
            return "ALREADY_PRESENT"
        raise PaperOperationError(
            "target appeared during import and differs from the catalog: "
            f"state={existing_state} actual={existing_detail or 'NONE'}"
        )
    except OSError as exc:
        raise PaperOperationError(f"atomic placement failed: {exc}") from exc
    return "INSTALLED"


def _copy_to_temp(source: Path, target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(
        prefix=f".{target.name}.", suffix=".tmp", dir=target.parent
    )
    temp_path = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as destination, source.open("rb") as origin:
            shutil.copyfileobj(origin, destination, CHUNK_SIZE)
            destination.flush()
            os.fsync(destination.fileno())
        return temp_path
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise


def run_import(
    data: dict[str, Any], root: Path, paper_id: str, source: Path, out: TextIO, err: TextIO
) -> int:
    papers = _schema_or_report(data, root, err)
    if papers is None:
        return 1
    matches = [paper for paper in papers if paper["id"] == paper_id]
    if not matches:
        print(f"[UNKNOWN_ID] id={paper_id}", file=err)
        return 1
    paper = matches[0]
    target = _target_path(root, paper)
    existing_state, existing_detail = inspect_file(target, paper["sha256"])
    if existing_state == "OK":
        print(f"papers import: ALREADY_PRESENT {_ref(paper)}", file=out)
        return 0
    if existing_state != "MISSING":
        print(
            f"[IMPORT_REFUSED] {_ref(paper)} existing_state={existing_state} "
            f"actual={existing_detail or 'NONE'} "
            "manual_action=move_existing_target_aside_and_reconcile_manually",
            file=err,
        )
        return 1
    if not source.exists() or not source.is_file():
        print(f"[IMPORT_SOURCE_INVALID] id={paper_id} source={source}", file=err)
        return 1

    temp_path: Path | None = None
    try:
        temp_path = _copy_to_temp(source, target)
        result = _atomic_commit(temp_path, target, paper["sha256"])
    except (OSError, PaperOperationError) as exc:
        print(
            f"[IMPORT_FAILED] {_ref(paper)} source={source} detail={exc}", file=err
        )
        return 1
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
    print(f"papers import: {result} {_ref(paper)}", file=out)
    return 0


def _download_to_temp(url: str, target: Path, timeout: float) -> Path:
    _validate_download_url(url)
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(
        prefix=f".{target.name}.download.", suffix=".tmp", dir=target.parent
    )
    temp_path = Path(name)
    bytes_written = 0
    try:
        request = Request(url, headers={"User-Agent": "paper-assets-sync/1.0"})
        opener = build_opener(StrictHTTPSRedirectHandler())
        with opener.open(request, timeout=timeout) as response, os.fdopen(
            descriptor, "wb"
        ) as destination:
            final_url = response.geturl()
            _validate_download_url(final_url)
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_DOWNLOAD_BYTES:
                raise PaperOperationError(
                    f"download exceeds {MAX_DOWNLOAD_BYTES} byte safety limit"
                )
            while True:
                chunk = response.read(CHUNK_SIZE)
                if not chunk:
                    break
                bytes_written += len(chunk)
                if bytes_written > MAX_DOWNLOAD_BYTES:
                    raise PaperOperationError(
                        f"download exceeds {MAX_DOWNLOAD_BYTES} byte safety limit"
                    )
                destination.write(chunk)
            destination.flush()
            os.fsync(destination.fileno())
        return temp_path
    except Exception:
        try:
            os.close(descriptor)
        except OSError:
            pass
        temp_path.unlink(missing_ok=True)
        raise


def _auto_download_eligible(paper: dict[str, Any]) -> bool:
    return bool(
        paper.get("download_url")
        and paper.get("acquisition_status") == "DIRECT_PUBLIC"
    )


def run_sync(
    data: dict[str, Any], root: Path, out: TextIO, err: TextIO, timeout: float = 30.0
) -> int:
    papers = _schema_or_report(data, root, err)
    if papers is None:
        return 1
    downloaded = 0
    manual = 0
    failed = 0
    for paper in papers:
        target = _target_path(root, paper)
        state, detail = inspect_file(target, paper["sha256"])
        if state == "OK" or (state == "MISSING" and not paper["required"]):
            continue
        if state != "MISSING":
            failed += 1
            print(
                f"[SYNC_REFUSED] {_ref(paper)} existing_state={state} "
                f"actual={detail or 'NONE'} manual_action=reconcile_existing_target",
                file=err,
            )
            continue
        if not _auto_download_eligible(paper):
            manual += 1
            print(
                f"[MANUAL_REQUIRED] {_ref(paper)} "
                f"acquisition_status={paper['acquisition_status']} "
                f"redistribution_status={paper['redistribution_status']} "
                f'manual_action="{_manual_action(paper)}"',
                file=err,
            )
            continue
        temp_path: Path | None = None
        try:
            temp_path = _download_to_temp(paper["download_url"], target, timeout)
            result = _atomic_commit(temp_path, target, paper["sha256"])
            if result == "INSTALLED":
                downloaded += 1
            print(f"papers sync: {result} {_ref(paper)}", file=out)
        except (HTTPError, URLError, OSError, ValueError, PaperOperationError) as exc:
            failed += 1
            print(
                f"[SYNC_FAILED] {_ref(paper)} detail={exc} "
                f'manual_action="{_manual_action(paper)}"',
                file=err,
            )
        finally:
            if temp_path is not None:
                temp_path.unlink(missing_ok=True)
    if manual or failed:
        print(
            f"papers sync: INCOMPLETE downloaded={downloaded} manual={manual} failed={failed}",
            file=err,
        )
        return 1
    print(f"papers sync: OK downloaded={downloaded}", file=out)
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scripts/papers", description="Manage cataloged research-paper PDFs safely."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "catalog-check",
        help="validate the public catalog/checksum contract without requiring PDFs",
    )
    subparsers.add_parser("doctor", help="validate catalog, required files, hashes, and PDF magic")
    subparsers.add_parser(
        "sync", help="download only explicitly eligible public PDFs; list all manual work"
    )
    import_parser = subparsers.add_parser(
        "import", help="verify and atomically import one cataloged PDF"
    )
    import_parser.add_argument("id", help="stable catalog paper ID")
    import_parser.add_argument("file", type=Path, help="local PDF to verify and import")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    root = Path(__file__).resolve().parent.parent
    catalog_path = root / "papers" / "catalog.yaml"
    try:
        data = load_catalog(catalog_path)
    except CatalogLoadError as exc:
        print(f"[CATALOG_ERROR] {exc}", file=sys.stderr)
        return 2
    if args.command == "doctor":
        return run_doctor(data, root, sys.stdout, sys.stderr)
    if args.command == "catalog-check":
        return run_catalog_check(
            data,
            root,
            root / "papers" / "checksums.sha256",
            sys.stdout,
            sys.stderr,
        )
    if args.command == "sync":
        return run_sync(data, root, sys.stdout, sys.stderr)
    if args.command == "import":
        return run_import(data, root, args.id, args.file, sys.stdout, sys.stderr)
    parser.error(f"unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
