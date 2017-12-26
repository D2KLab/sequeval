from abc import ABC
from abc import abstractmethod

import numpy as np


class Recommender(ABC):

    def __init__(self, training_set, items):
        self.training_set = training_set
        self.items = items
        # Dictionary to store the recommended sequences
        self.cache = {}

    def recommend(self, seed_rating, k):
        """
        Generate a recommended sequence of length k from a seed rating.

        :param seed_rating: The seed rating.
        :param k: The length of the sequence.
        :return: A recommended sequence.
        """
        try:
            # If this sequence has already been generated
            return list(self.cache[(seed_rating, k)])
        except KeyError:
            pass

        current_rating = seed_rating
        sequence = []

        for i in range(0, k):
            # The probabilities for the next item of the sequence
            prediction = self.predict(current_rating)
            # noinspection PyUnresolvedReferences
            item_index = np.random.multinomial(1, prediction).argmax()
            next_rating = (self.items[item_index], current_rating[1], current_rating[2] + 1)
            sequence.append(next_rating)
            current_rating = next_rating

        # After each sequence the model needs to be reset
        self.reset()

        # Save this sequence in the cache
        self.cache[(seed_rating, k)] = sequence

        return sequence

    def predict_item(self, rating, item):
        """
        Given the current rating of the recommended sequence, predict
        the probability that the following rating will contain this item.

        :param rating: The current rating of the recommended sequence.
        :param item: The next item of the sequence.
        :return: A probability.
        """
        prediction = self.predict(rating)
        return prediction[self.items.index(item)]

    @abstractmethod
    def predict(self, rating):
        """
        Given the current rating of the recommended sequence, predict
        the probabilities for all the possible items of being in the next rating.

        :param rating: The current rating of the recommended sequence.
        :return: An array of probabilities.
        :rtype: Iterable.
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset the internal model that represents the current sequence.
        """
        pass
