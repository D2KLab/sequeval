from abc import ABC
from abc import abstractmethod

import numpy as np
import scipy.spatial.distance as distance


class Similarity(ABC):

    def __init__(self, items):
        self.items = items

    @abstractmethod
    def similarity(self, item_i, item_j):
        """
        Compute a similarity metric between two items.

        :param item_i: The first item.
        :param item_j: The second item.
        :return: A similarity value.
        """
        pass


class CosineSimilarity(Similarity):

    def __init__(self, training_set, items):
        super().__init__(items)

        # Create an item sequence matrix
        self.matrix = np.full((len(self.items), len(training_set)), 0)

        for sequence_index, sequence in enumerate(training_set):
            for rating in sequence:
                item_index = self.items.index(rating[0])
                self.matrix[item_index, sequence_index] += 1

    def similarity(self, item_i, item_j):
        """
        Compute the cosine similarity between two items.

        :param item_i: The first item.
        :param item_j: The second item.
        :return: A cosine similarity value.
        """
        index_i = self.items.index(item_i)
        index_j = self.items.index(item_j)
        return 1 - distance.cosine(self.matrix[index_i], self.matrix[index_j])
