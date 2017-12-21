import numpy as np

from .unigram import UnigramRecommender


class MostPopularRecommender(UnigramRecommender):
    name = 'Most popular'

    def __init__(self, training_set, items):
        super().__init__(training_set, items)

        # Sort indexes in descending order
        self.sorted_weights = np.argsort(-self.weights)

        self.model = 0

    def predict(self, rating):
        prediction = np.full(len(self.items), 0.0, dtype=float)
        model_index = self.sorted_weights[self.model]
        prediction[model_index] = 1.0
        self.model += 1
        return prediction

    def reset(self):
        self.model = 0
