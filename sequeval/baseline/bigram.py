import numpy as np

from ..recommender import Recommender


class BigramRecommender(Recommender):
    name = 'Bigram'

    def __init__(self, training_set, items):
        super().__init__(training_set, items)

        # The matrix is initialized to 1.0
        self.bigrams = np.full((len(self.items), len(self.items)), 1.0, dtype=float)

        for sequence in self.training_set:
            previous_item_index = None

            for rating in sequence:
                item_index = self.items.index(rating[0])

                if previous_item_index is not None:
                    self.bigrams[previous_item_index, item_index] += 1

                previous_item_index = item_index

        # Probability normalization
        for row in self.bigrams:
            row /= row.sum()

    def predict(self, rating):
        item_index = self.items.index(rating[0])
        return self.bigrams[item_index]

    def reset(self):
        pass
