#!/usr/bin/env python3
"""Run deterministic, simulation-only replay-oracle counterexamples."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable


EXPERIMENT_ID = "EXP-001"
DATASET_ID = "DATA-D1-REPLAY-ORACLES-V1"
EVIDENCE_LABEL = "simulation-only"


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inversion_count(values: Iterable[int]) -> int:
    sequence = list(values)
    return sum(
        1
        for left in range(len(sequence))
        for right in range(left + 1, len(sequence))
        if sequence[left] > sequence[right]
    )


def adjacent_descents(values: Iterable[int]) -> int:
    sequence = list(values)
    return sum(left > right for left, right in zip(sequence, sequence[1:]))


def first_divergence(expected: list[int], observed: list[int]) -> dict[str, int | None]:
    common_length = min(len(expected), len(observed))
    for index in range(common_length):
        if expected[index] != observed[index]:
            return {
                "position_1_based": index + 1,
                "expected_sequence": expected[index],
                "observed_sequence": observed[index],
            }
    if len(expected) != len(observed):
        return {
            "position_1_based": common_length + 1,
            "expected_sequence": expected[common_length] if common_length < len(expected) else None,
            "observed_sequence": observed[common_length] if common_length < len(observed) else None,
        }
    return {"position_1_based": None, "expected_sequence": None, "observed_sequence": None}


def _initial_state() -> dict[str, Any]:
    return {
        "answer": None,
        "eliminated": [],
        "scroll_y": 0,
        "visibility": "visible",
        "submitted": False,
    }


def _apply_event(state: dict[str, Any], event: dict[str, Any]) -> dict[str, Any]:
    next_state = copy.deepcopy(state)
    event_type = event["type"]
    payload = event.get("payload", {})
    if event_type == "answer":
        next_state["answer"] = payload["value"]
    elif event_type == "eliminate":
        next_state["eliminated"] = sorted(set(next_state["eliminated"]) | {payload["value"]})
    elif event_type == "restore":
        next_state["eliminated"] = [
            value for value in next_state["eliminated"] if value != payload["value"]
        ]
    elif event_type == "scroll":
        next_state["scroll_y"] = payload["y"]
    elif event_type == "visibility":
        next_state["visibility"] = payload["value"]
    elif event_type == "submit":
        next_state["submitted"] = True
    elif event_type != "start":
        raise ValueError(f"unknown event type: {event_type}")
    return next_state


def replay(events: list[dict[str, Any]]) -> dict[str, Any]:
    state = _initial_state()
    trajectory: list[dict[str, Any]] = []
    for event in events:
        state = _apply_event(state, event)
        trajectory.append(copy.deepcopy(state))
    return {"final_state": state, "trajectory": trajectory}


def _base_events() -> list[dict[str, Any]]:
    event_specs = [
        (1, "start", {}),
        (2, "answer", {"value": "A"}),
        (3, "eliminate", {"value": "B"}),
        (4, "scroll", {"y": 640}),
        (5, "restore", {"value": "B"}),
        (6, "answer", {"value": "C"}),
        (7, "answer", {"value": "D"}),
        (8, "submit", {}),
    ]
    return [
        {"event_id": f"evt-{sequence}", "sequence": sequence, "type": event_type, "payload": payload}
        for sequence, event_type, payload in event_specs
    ]


def simulate_event_corruption() -> dict[str, Any]:
    expected = _base_events()
    by_sequence = {event["sequence"]: event for event in expected}
    observed = [copy.deepcopy(by_sequence[sequence]) for sequence in [1, 2, 3, 5, 5, 7, 6, 8]]
    expected_ids = {event["event_id"] for event in expected}
    observed_ids = [event["event_id"] for event in observed]
    unique_observed_ids = set(observed_ids)
    missing = sorted(event["sequence"] for event in expected if event["event_id"] not in unique_observed_ids)
    duplicate_instances = len(observed_ids) - len(unique_observed_ids)
    arrival_sequences = [event["sequence"] for event in observed]
    first_occurrence = list(dict.fromkeys(arrival_sequences))
    ordered_deduplicated = sorted(
        {event["event_id"]: event for event in observed}.values(), key=lambda event: event["sequence"]
    )
    expected_replay = replay(expected)
    arrival_replay = replay(observed)
    sequence_replay = replay(ordered_deduplicated)
    return {
        "evidence_label": EVIDENCE_LABEL,
        "injected_truth": {"missing_sequences": [4], "duplicate_instances": 1, "reordered_pair": [7, 6]},
        "metrics": {
            "unique_event_coverage": len(unique_observed_ids & expected_ids) / len(expected_ids),
            "missing_sequences": missing,
            "duplicate_instances": duplicate_instances,
            "inversion_count": inversion_count(first_occurrence),
            "adjacent_descents": adjacent_descents(arrival_sequences),
            "first_stream_divergence": first_divergence(
                [event["sequence"] for event in expected], arrival_sequences
            ),
        },
        "oracles": {
            "arrival_full_final_state_equal": arrival_replay["final_state"]
            == expected_replay["final_state"],
            "sequence_reconstructed_full_final_state_equal": sequence_replay["final_state"]
            == expected_replay["final_state"],
            "sequence_reconstructed_semantic_final_state_equal": {
                key: sequence_replay["final_state"][key]
                for key in ("answer", "eliminated", "submitted")
            }
            == {
                key: expected_replay["final_state"][key]
                for key in ("answer", "eliminated", "submitted")
            },
        },
    }


def simulate_final_state_blind_spot() -> dict[str, Any]:
    reference = [
        {"event_id": "ref-1", "sequence": 1, "type": "answer", "payload": {"value": "A"}},
        {"event_id": "ref-2", "sequence": 2, "type": "answer", "payload": {"value": "B"}},
    ]
    candidate = [
        {"event_id": "candidate-1", "sequence": 1, "type": "answer", "payload": {"value": "B"}}
    ]
    reference_replay = replay(reference)
    candidate_replay = replay(candidate)
    final_state_equal = candidate_replay["final_state"] == reference_replay["final_state"]
    event_stream_equal = [event["payload"]["value"] for event in candidate] == [
        event["payload"]["value"] for event in reference
    ]
    trajectory_equal = candidate_replay["trajectory"] == reference_replay["trajectory"]
    return {
        "evidence_label": EVIDENCE_LABEL,
        "reference_process": ["A", "B"],
        "candidate_process": ["B"],
        "oracles": {
            "final_state_equal": final_state_equal,
            "event_stream_equal": event_stream_equal,
            "state_trajectory_equal": trajectory_equal,
            "final_state_only_false_negative": final_state_equal
            and (not event_stream_equal or not trajectory_equal),
        },
    }


def simulate_time_fields() -> dict[str, Any]:
    by_sequence = {
        sequence: {"sequence": sequence, "wall_time": wall_time, "mono_ms": mono_ms}
        for sequence, wall_time, mono_ms in zip(
            [1, 2, 3, 4, 5], [1000, 1005, 1002, 1008, 1008], [0, 5, 5, 10, 15]
        )
    }
    arrival = [copy.deepcopy(by_sequence[sequence]) for sequence in [1, 3, 2, 5, 4]]

    def ordered_sequences(field: str | None) -> list[int]:
        ordered = arrival if field is None else sorted(arrival, key=lambda event: event[field])
        return [event["sequence"] for event in ordered]

    orders = {
        "arrival": ordered_sequences(None),
        "wall_time_only": ordered_sequences("wall_time"),
        "mono_ms_only": ordered_sequences("mono_ms"),
        "sequence": ordered_sequences("sequence"),
    }
    return {
        "evidence_label": EVIDENCE_LABEL,
        "events_in_arrival_order": arrival,
        "orders": orders,
        "inversion_counts": {name: inversion_count(values) for name, values in orders.items()},
        "field_roles": {
            "wall_time": "calendar/cross-system anchor; can roll back or tie",
            "mono_ms": "within-execution elapsed time; can tie after coarsening and is not cross-execution",
            "sequence": "session-local total order and deterministic replay key",
        },
    }


def run_simulations() -> dict[str, Any]:
    results = {
        "schema_version": 1,
        "experiment_id": EXPERIMENT_ID,
        "dataset_id": DATASET_ID,
        "evidence_label": EVIDENCE_LABEL,
        "scenarios": {
            "event_corruption": simulate_event_corruption(),
            "final_state_blind_spot": simulate_final_state_blind_spot(),
            "time_fields": simulate_time_fields(),
        },
    }
    event_metrics = results["scenarios"]["event_corruption"]["metrics"]
    event_oracles = results["scenarios"]["event_corruption"]["oracles"]
    blind_oracles = results["scenarios"]["final_state_blind_spot"]["oracles"]
    time_inversions = results["scenarios"]["time_fields"]["inversion_counts"]
    checks = {
        "event_missing_detected": event_metrics["missing_sequences"] == [4],
        "event_duplicate_detected": event_metrics["duplicate_instances"] == 1,
        "event_reordering_detected": event_metrics["inversion_count"] == 1
        and event_metrics["adjacent_descents"] == 1,
        "event_coverage_correct": event_metrics["unique_event_coverage"] == 0.875,
        "first_divergence_correct": event_metrics["first_stream_divergence"]["position_1_based"]
        == 4,
        "arrival_state_mismatch_detected": event_oracles["arrival_full_final_state_equal"] is False,
        "missing_scroll_detected_after_sequence_replay": event_oracles[
            "sequence_reconstructed_full_final_state_equal"
        ]
        is False,
        "semantic_final_state_can_still_match": event_oracles[
            "sequence_reconstructed_semantic_final_state_equal"
        ]
        is True,
        "final_state_blind_spot_reproduced": blind_oracles
        == {
            "final_state_equal": True,
            "event_stream_equal": False,
            "state_trajectory_equal": False,
            "final_state_only_false_negative": True,
        },
        "time_field_inversions_correct": time_inversions
        == {"arrival": 2, "wall_time_only": 2, "mono_ms_only": 1, "sequence": 0},
    }
    results["predeclared_checks"] = checks
    results["status"] = "COMPLETE" if all(checks.values()) else "INVALID"
    return results


def _git_value(repo_root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=repo_root, check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def _yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def write_run(output_dir: Path, repo_root: Path, run_id: str) -> dict[str, Any]:
    started_at = dt.datetime.now(dt.timezone.utc)
    results = run_simulations()
    output_dir.mkdir(parents=True, exist_ok=False)
    results_path = output_dir / "results.json"
    results_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    finished_at = dt.datetime.now(dt.timezone.utc)
    config_path = Path(__file__).with_name("simulation_config.json")
    fixture_hash = _sha256_bytes(_canonical_json(results["scenarios"]))
    dirty = bool(_git_value(repo_root, "status", "--porcelain"))
    manifest = {
        "schema_version": 1,
        "experiment_id": EXPERIMENT_ID,
        "run_id": run_id,
        "status": results["status"],
        "started_at": started_at.isoformat(),
        "finished_at": finished_at.isoformat(),
        "git_commit": _git_value(repo_root, "rev-parse", "HEAD"),
        "git_dirty": dirty,
        "catalog_sha256": _sha256_file(repo_root / "sources" / "catalog.yaml"),
        "checksums_manifest_sha256": _sha256_file(repo_root / "sources" / "checksums.sha256"),
        "dataset_id": DATASET_ID,
        "dataset_manifest_sha256": fixture_hash,
        "data_role": "DATA-D1 engineering synthetic; simulation-only",
        "configuration_path": config_path.relative_to(repo_root).as_posix(),
        "configuration_sha256": _sha256_file(config_path),
        "runtime": sys.version.split()[0],
        "metric_registry_version": "replay-fidelity-oracles/v1",
        "results_path": results_path.relative_to(repo_root).as_posix(),
        "results_sha256": _sha256_file(results_path),
        "failure_reason": None if results["status"] == "COMPLETE" else "predeclared check failed",
    }
    manifest_lines = [
        "schema_version: 1",
        f"experiment_id: {_yaml_scalar(manifest['experiment_id'])}",
        f"run_id: {_yaml_scalar(manifest['run_id'])}",
        f"status: {_yaml_scalar(manifest['status'])}",
        f"started_at: {_yaml_scalar(manifest['started_at'])}",
        f"finished_at: {_yaml_scalar(manifest['finished_at'])}",
        "git:",
        f"  commit: {_yaml_scalar(manifest['git_commit'])}",
        f"  dirty: {_yaml_scalar(manifest['git_dirty'])}",
        "sources:",
        f"  catalog_sha256: {_yaml_scalar(manifest['catalog_sha256'])}",
        f"  checksums_manifest_sha256: {_yaml_scalar(manifest['checksums_manifest_sha256'])}",
        "data:",
        f"  dataset_ids: [{_yaml_scalar(manifest['dataset_id'])}]",
        f"  manifest_sha256: {_yaml_scalar(manifest['dataset_manifest_sha256'])}",
        f"  role: {_yaml_scalar(manifest['data_role'])}",
        "configuration:",
        f"  path: {_yaml_scalar(manifest['configuration_path'])}",
        f"  sha256: {_yaml_scalar(manifest['configuration_sha256'])}",
        "split:",
        "  manifest_sha256: null",
        "seeds: []",
        "environment:",
        "  lockfile_sha256: null",
        f"  container_or_runtime: {_yaml_scalar('Python ' + manifest['runtime'])}",
        "metrics:",
        f"  registry_version: {_yaml_scalar(manifest['metric_registry_version'])}",
        "outputs:",
        f"  - path: {_yaml_scalar(manifest['results_path'])}",
        f"    sha256: {_yaml_scalar(manifest['results_sha256'])}",
        f"failure_reason: {_yaml_scalar(manifest['failure_reason'])}",
    ]
    (output_dir / "run-manifest.yaml").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--run-id", default="2026-08-16-simulation-only-v1")
    args = parser.parse_args()
    if args.output_dir is None:
        print(json.dumps(run_simulations(), ensure_ascii=False, indent=2))
        return 0
    manifest = write_run(args.output_dir.resolve(), args.repo_root.resolve(), args.run_id)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if manifest["status"] == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
