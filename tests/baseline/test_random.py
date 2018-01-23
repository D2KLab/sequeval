import unittest

import numpy as np

import sequeval.baseline as baseline
from ..test_builder import sequences, items


class MostPopularTestSuite(unittest.TestCase):

    def test_predict(self):
        random = baseline.RandomRecommender(sequences, items)
        expected = np.full(len(items), 1 / 3, dtype=float)
        self.assertEqual(expected.tolist(), random.predict(None).tolist())
        random.reset()
        self.assertEqual(expected.tolist(), random.predict(None).tolist())


if __name__ == '__main__':
    unittest.main()
