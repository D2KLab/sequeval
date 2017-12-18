import unittest

import sequeval
import sequeval.baseline as baseline
from .test_builder import sequences as training_set, items

test_set = [[(1, 1, 0), (1, 1, 1), (2, 1, 2), (3, 1, 3)],
            [(1, 1, 0), (1, 1, 1), (2, 1, 2), (1, 1, 3)]]


class RecommenderTestSuite(unittest.TestCase):

    def test_coverage(self):
        recommender = baseline.MostPopularRecommender(training_set, items)
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertEqual(3 / 3, evaluator.coverage(recommender))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertEqual(2 / 3, evaluator.coverage(recommender))

    def test_precision(self):
        recommender = baseline.MostPopularRecommender(training_set, items)
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertAlmostEqual(5 / 6, evaluator.precision(recommender))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertEqual(1.0, evaluator.precision(recommender))

    def test_ndpm(self):
        recommender = baseline.MostPopularRecommender(training_set, items)
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertAlmostEqual(5 / 12, evaluator.ndpm(recommender))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertEqual(3 / 4, evaluator.ndpm(recommender))

    def test_diversity(self):
        pass

    def test_novelty(self):
        pass

    def test_serendipity(self):
        pass

    def test_confidence(self):
        pass

    def test_perplexity(self):
        pass


if __name__ == '__main__':
    unittest.main()
