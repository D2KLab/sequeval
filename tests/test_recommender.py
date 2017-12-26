import unittest

import sequeval.baseline as baseline
from .test_builder import sequences, items


class RecommenderTestSuite(unittest.TestCase):

    def test_recommend(self):
        recommender = baseline.MostPopularRecommender(sequences, items)
        expected = [(2, 1, 4), (1, 1, 5), (3, 1, 6)]
        self.assertEqual(expected, recommender.recommend((1, 1, 3), 3))
        # Check that there is no memory
        self.assertEqual(expected, recommender.recommend((1, 1, 3), 3))

    def test_predict_item(self):
        recommender = baseline.MostPopularRecommender(sequences, items)
        self.assertEqual(1.0, recommender.predict_item((1, 1, 3), 2))
        self.assertEqual(1.0, recommender.predict_item((1, 1, 4), 1))
        self.assertEqual(0.0, recommender.predict_item((1, 1, 5), 1))


if __name__ == '__main__':
    unittest.main()
