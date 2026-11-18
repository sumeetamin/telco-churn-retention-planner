import unittest

from score import ranked_positions


class RankingTests(unittest.TestCase):
    def test_contact_share_and_stable_tie_order(self):
        self.assertEqual(ranked_positions([0.2, 0.9, 0.9, 0.1], 0.5).tolist(), [1, 2])
        self.assertEqual(ranked_positions([0.2, 0.9, 0.1], 0.01).tolist(), [1])

    def test_rejects_invalid_share_and_scores(self):
        for share in (0, 1.1):
            with self.assertRaises(ValueError):
                ranked_positions([0.1, 0.2], share)
        with self.assertRaises(ValueError):
            ranked_positions([], 0.5)
        with self.assertRaises(ValueError):
            ranked_positions([0.1, float("nan")], 0.5)


if __name__ == "__main__":
    unittest.main()
