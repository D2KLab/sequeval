import unittest

import sequeval.baseline as baseline
from ..test_builder import sequences, items


class MostPopularTestSuite(unittest.TestCase):

    def test_predict(self):
        unigram = baseline.UnigramRecommender(sequences, items)
        expected = [0.375, 0.5, 0.125]
        self.assertEqual(expected, unigram.predict(None).tolist())
        self.assertEqual(expected, unigram.predict(None).tolist())


if __name__ == '__main__':
    unittest.main()
