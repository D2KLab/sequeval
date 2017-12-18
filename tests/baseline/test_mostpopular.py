import unittest

import numpy as np

import sequeval.baseline as baseline
from ..test_builder import sequences, items


class MostPopularTestSuite(unittest.TestCase):

    def test_predict(self):
        most_popular = baseline.MostPopularRecommender(sequences, items)

        # First item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(2)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())

        # Second item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(1)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())

        # Third item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(3)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())

    def test_reset(self):
        most_popular = baseline.MostPopularRecommender(sequences, items)

        # First item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(2)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())

        # Second item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(1)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())

        # Reset
        most_popular.reset()

        # First item
        expected = np.full(len(items), 0.0, dtype=float)
        expected[items.index(2)] = 1.0
        self.assertEqual(expected.tolist(), most_popular.predict(None).tolist())


if __name__ == '__main__':
    unittest.main()
