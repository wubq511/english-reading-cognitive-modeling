from pathlib import Path
import importlib.util
import json
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_evals", ROOT / "scripts" / "skill_evals.py")
EVALS = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(EVALS)


class SkillEvalTests(unittest.TestCase):
    def test_all_entry_skill_eval_suites_are_valid(self):
        self.assertEqual([], EVALS.validate_all())
        self.assertEqual(18, EVALS.total_evals())

    def test_implicit_prompt_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = EVALS.eval_path("ercm-implement", root)
            target.parent.mkdir(parents=True)
            target.write_text(
                json.dumps(
                    {
                        "skill_name": "ercm-implement",
                        "evals": [
                            {
                                "id": index,
                                "prompt": "Please pick a ticket",
                                "expected_output": "Refuse",
                                "expectations": ["No ticket is selected", "No work is done"],
                            }
                            for index in range(1, 5)
                        ],
                    }
                ),
                encoding="utf-8",
            )
            errors = EVALS.validate_eval_suite("ercm-implement", root)
            self.assertEqual(4, sum("eval-must-explicitly-invoke-skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
