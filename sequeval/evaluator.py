class Evaluator:

    def __init__(self, training_set, test_set, items, k):
        self.training_set = training_set
        self.test_set = test_set
        self.items = items
        self.k = k

    def coverage(self, recommender):
        pass

    def precision(self, recommender):
        pass

    def ndpm(self, recommender):
        pass

    def diversity(self, recommender):
        pass

    def novelty(self, recommender):
        pass

    def serendipity(self, recommender):
        pass

    def confidence(self, recommender):
        pass

    def perplexity(self, recommender):
        pass
