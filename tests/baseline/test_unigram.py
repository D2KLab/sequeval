import unittest

import sequeval.baseline as baseline
from ..test_builder import sequences, items


class MostPopularTestSuite(unittest.TestCase):

    def test_predict(self):
        unigram = baseline.UnigramRecommender(sequences, items)
        expected = [4 / 11, 5 / 11, 2 / 11]
        self.assertEqual(expected, unigram.predict(None).tolist())
        self.assertEqual(expected, unigram.predict(None).tolist())


if __name__ == '__main__':
    unittest.main()
