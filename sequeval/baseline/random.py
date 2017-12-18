import numpy as np

from ..recommender import Recommender


class RandomRecommender(Recommender):

    def predict(self, rating):
        return np.full(len(self.items), 1 / len(self.items), dtype=float)

    def reset(self):
        pass
