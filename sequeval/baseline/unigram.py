import numpy as np

from ..recommender import Recommender


class UnigramRecommender(Recommender):

    def __init__(self, training_set, items):
        super().__init__(training_set, items)

        self.weights = np.full(len(self.items), 0.0, dtype=float)

        for sequence in training_set:
            for rating in sequence:
                item_index = self.items.index(rating[0])
                self.weights[item_index] += 1

        self.weights /= self.weights.sum()

    def predict(self, rating):
        return self.weights

    def reset(self):
        pass
