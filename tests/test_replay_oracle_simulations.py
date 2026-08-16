from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    REPO_ROOT
    / "experiments"
    / "specs"
    / "EXP-001-replay-oracle-simulations"
    / "simulate.py"
)
SPEC = importlib.util.spec_from_file_location("replay_oracle_simulations", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
SIMULATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SIMULATION)


class ReplayOracleSimulationTests(unittest.TestCase):
    def test_inversion_count(self) -> None:
        self.assertEqual(SIMULATION.inversion_count([1, 3, 2, 5, 4]), 2)

    def test_event_corruption_recovers_injected_truth(self) -> None:
        result = SIMULATION.simulate_event_corruption()
        self.assertEqual(result["metrics"]["missing_sequences"], [4])
        self.assertEqual(result["metrics"]["duplicate_instances"], 1)
        self.assertEqual(result["metrics"]["inversion_count"], 1)
        self.assertEqual(result["metrics"]["adjacent_descents"], 1)
        self.assertEqual(result["metrics"]["unique_event_coverage"], 0.875)

    def test_final_state_only_oracle_has_blind_spot(self) -> None:
        oracles = SIMULATION.simulate_final_state_blind_spot()["oracles"]
        self.assertTrue(oracles["final_state_equal"])
        self.assertFalse(oracles["event_stream_equal"])
        self.assertFalse(oracles["state_trajectory_equal"])
        self.assertTrue(oracles["final_state_only_false_negative"])

    def test_sequence_is_only_exact_frozen_total_order(self) -> None:
        result = SIMULATION.simulate_time_fields()
        self.assertEqual(
            result["inversion_counts"],
            {"arrival": 2, "wall_time_only": 2, "mono_ms_only": 1, "sequence": 0},
        )
        self.assertEqual(result["orders"]["sequence"], [1, 2, 3, 4, 5])

    def test_all_predeclared_checks_pass(self) -> None:
        result = SIMULATION.run_simulations()
        self.assertEqual(result["evidence_label"], "simulation-only")
        self.assertEqual(result["status"], "COMPLETE")
        self.assertTrue(all(result["predeclared_checks"].values()))


if __name__ == "__main__":
    unittest.main()
