import math
import unittest

import sequeval
import sequeval.baseline as baseline
from .test_builder import sequences as training_set, items

test_set = [[(1, 1, 0), (1, 1, 1), (2, 1, 2), (3, 1, 3)],
            [(1, 1, 0), (1, 1, 1), (2, 1, 2), (1, 1, 3)]]


class EvaluatorTestSuite(unittest.TestCase):

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
        recommender = baseline.MostPopularRecommender(training_set, items)
        similarity = sequeval.CosineSimilarity(training_set, items)

        # Compute the possible diversities
        d1 = 1 - similarity.similarity(2, 1)
        d2 = 1 - similarity.similarity(2, 3)
        d3 = 1 - similarity.similarity(1, 3)

        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertAlmostEqual((d1 + d2 + d3) / 3, evaluator.diversity(recommender, similarity))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertAlmostEqual(d1, evaluator.diversity(recommender, similarity))

    def test_novelty(self):
        recommender = baseline.MostPopularRecommender(training_set, items)
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertAlmostEqual((math.log2(0.375) + math.log2(0.5) + math.log2(0.125)) / -3,
                               evaluator.novelty(recommender))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertAlmostEqual((math.log2(0.375) + math.log2(0.5)) / -2, evaluator.novelty(recommender))

    def test_serendipity(self):
        recommender = baseline.MostPopularRecommender(training_set, items)
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        self.assertEqual(0.0, evaluator.serendipity(recommender))
        self.assertAlmostEqual(1 / 6, evaluator.serendipity(recommender, primitive_k=2))
        evaluator = sequeval.Evaluator(training_set, test_set, items, 2)
        self.assertEqual(0.0, evaluator.serendipity(recommender))
        self.assertAlmostEqual(3 / 6, evaluator.serendipity(recommender, primitive_k=1))

    def test_confidence(self):
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        recommender = baseline.MostPopularRecommender(training_set, items)
        self.assertEqual(1.0, evaluator.confidence(recommender))
        recommender = baseline.RandomRecommender(training_set, items)
        self.assertAlmostEqual(1 / 3, evaluator.confidence(recommender))

    def test_perplexity(self):
        evaluator = sequeval.Evaluator(training_set, test_set, items, 3)
        recommender = baseline.MostPopularRecommender(training_set, items)
        self.assertAlmostEqual(math.inf, evaluator.perplexity(recommender))
        recommender = baseline.RandomRecommender(training_set, items)
        self.assertAlmostEqual(3.0, evaluator.perplexity(recommender))


if __name__ == '__main__':
    unittest.main()
