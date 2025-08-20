import unittest
from find_missing_ranges import find_missing_ranges

class TestFindMissingRanges(unittest.TestCase):
    def test_example(self):
        frames = [1, 2, 3, 5, 6, 10, 11, 16]
        self.assertEqual(
            find_missing_ranges(frames),
            {
                "gaps": [[4, 4], [7, 9], [12, 15]],
                "longest_gap": [12, 15],
                "missing_count": 8,
            },
        )

    def test_no_missing(self):
        frames = [3, 2, 1, 4, 5]  # unordered, complete 1..5
        self.assertEqual(
            find_missing_ranges(frames),
            {"gaps": [], "longest_gap": None, "missing_count": 0},
        )

    def test_missing_at_start(self):
        frames = [3, 4, 5]  # expected total 5
        self.assertEqual(
            find_missing_ranges(frames),
            {"gaps": [[1, 2]], "longest_gap": [1, 2], "missing_count": 2},
        )

    def test_missing_internal(self):
        frames = [1, 4, 5, 8]  # expected total 8
        self.assertEqual(
            find_missing_ranges(frames),
            {"gaps": [[2, 3], [6, 7]], "longest_gap": [2, 3], "missing_count": 4},
        )

    def test_single_frame(self):
        self.assertEqual(
            find_missing_ranges([1]),
            {"gaps": [], "longest_gap": None, "missing_count": 0},
        )

    def test_only_high_frame(self):
        self.assertEqual(
            find_missing_ranges([2]),
            {"gaps": [[1, 1]], "longest_gap": [1, 1], "missing_count": 1},
        )

    def test_empty(self):
        self.assertEqual(
            find_missing_ranges([]),
            {"gaps": [], "longest_gap": None, "missing_count": 0},
        )

if __name__ == "__main__":
    unittest.main()
