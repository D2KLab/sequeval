import unittest

import sequeval.baseline as baseline
from ..test_builder import sequences, items


class BigramTestSuite(unittest.TestCase):

    def test_predict(self):
        bigram = baseline.BigramRecommender(sequences, items)

        # First item
        expected = [1 / 5, 3 / 5, 1 / 5]
        self.assertEqual(expected, bigram.predict((1, 1, 1)).tolist())
        bigram.reset()

        # Second item
        expected = [2 / 5, 2 / 5, 1 / 5]
        self.assertEqual(expected, bigram.predict((2, 1, 1)).tolist())
        bigram.reset()

        # Third item
        expected = [1 / 4, 2 / 4, 1 / 4]
        self.assertEqual(expected, bigram.predict((3, 1, 1)).tolist())


if __name__ == '__main__':
    unittest.main()
