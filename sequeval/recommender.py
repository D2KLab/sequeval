from abc import ABC
from abc import abstractmethod


class Recommender(ABC):

    def __init__(self, training_set, items):
        self.training_set = training_set
        self.items = items

    def generate(self, seed_rating, k):
        """
        Generate a recommended sequence of length k from a seed rating.

        :param seed_rating: The seed rating.
        :param k: The length of the sequence.
        :return: A recommended sequence.
        """
        pass

    def predict_item(self, rating, item):
        """
        Given the current rating of the recommended sequence, predict
        the probability that the following rating will contain this item.

        :param rating: The current rating of the recommended sequence.
        :param item: The next item of the sequence.
        :return: A probability.
        """
        pass

    @abstractmethod
    def predict(self, rating):
        """
        Given the current rating of the recommended sequence, predict
        the probabilities for all the possible items of being in the next rating.

        :param rating: The current rating of the recommended sequence.
        :return: An array of probabilities.
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset the internal model that represents the current sequence.
        """
        pass
