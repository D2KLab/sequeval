import math
import unittest

import sequeval
from .test_builder import sequences as training_set, items


class SimilarityTestSuite(unittest.TestCase):

    def test_cosine_similarity(self):
        cosine = sequeval.CosineSimilarity(training_set, items + [4])
        self.assertAlmostEqual(4 / (math.sqrt(5) * math.sqrt(6)), cosine.similarity(1, 2))
        self.assertAlmostEqual(0, cosine.similarity(1, 3))
        self.assertAlmostEqual(1 / (math.sqrt(6)), cosine.similarity(2, 3))
        self.assertAlmostEqual(0, cosine.similarity(1, 4))


if __name__ == '__main__':
    unittest.main()
