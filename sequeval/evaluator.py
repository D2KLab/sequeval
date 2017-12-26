import itertools
import math

import numpy as np

import sequeval.baseline as baseline


class Evaluator:

    def __init__(self, training_set, test_set, items, k):
        self.training_set = training_set
        self.test_set = test_set
        self.items = items
        self.k = k

        self.users = self._get_user_set(training_set + test_set)
        self.distribution = self._get_distribution(training_set, items)

    @staticmethod
    def _get_item_list(sequence):
        """
        Convert a sequence in a list of items.

        :param sequence: A list of ratings.
        :return: A list of items.
        """
        items = []

        for rating in sequence:
            items.append(rating[0])

        return items

    @staticmethod
    def _get_user_set(sequences):
        """
        Create an ordered list of unique users from a list of sequences.

        :param sequences: A list of sequences.
        :return: An ordered list of unique users.
        """
        users = []

        for sequence in sequences:
            for rating in sequence:
                users.append(rating)

        return sorted(list(set(users)))

    @staticmethod
    def _get_distribution(sequences, items):
        """
        Get an array representing the number of times the items
        appeared in a list of sequences.

        :param sequences: The list of sequences.
        :param items: The list of items.
        :return: An array representing the distribution.
        """
        distribution = np.full(len(items), 0.0, dtype=float)

        for sequence in sequences:
            for rating in sequence:
                item_index = items.index(rating[0])
                distribution[item_index] += 1

        distribution /= distribution.sum()

        return distribution

    def coverage(self, recommender):
        recommended_items = []

        # For each sequence in the test set
        for sequence in self.test_set:
            recommended_sequence = recommender.recommend(sequence[0], self.k)

            for rating in recommended_sequence:
                recommended_items.append(rating[0])

        coverage = len(set(recommended_items)) / len(self.items)

        return coverage

    def precision(self, recommender):
        precision = np.full(len(self.test_set), 0.0, dtype=float)

        # For each sequence in the test set
        for sequence_index, sequence in enumerate(self.test_set):
            local_k = min(self.k, len(sequence) - 1)
            hit = 0

            recommended_sequence = recommender.recommend(sequence[0], self.k)
            reference_items = self._get_item_list(sequence[1:])

            # For each rating in the recommended sequence
            for rating in recommended_sequence:
                # Check if the item is also in the reference path
                if rating[0] in reference_items:
                    # Only the first time
                    reference_items.remove(rating[0])
                    hit += 1

            precision[sequence_index] = hit / local_k

        return precision.mean()

    def ndpm(self, recommender):
        def count_item(item, item_list):
            return len(list(filter(lambda x: x == item, item_list)))

        ndpm = np.full(len(self.test_set), 0.0, dtype=float)

        for sequence_index, sequence in enumerate(self.test_set):
            recommended_sequence = recommender.recommend(sequence[0], self.k)
            recommended_items = self._get_item_list(recommended_sequence)
            reference_items = self._get_item_list(sequence[1:])

            metric = 0
            worst_case = 0

            for items in itertools.combinations(recommended_items, 2):
                # If the two items are in the recommended sequence and they are unique
                if count_item(items[0], reference_items) == 1 and count_item(items[1], reference_items) == 1:
                    index_i = reference_items.index(items[0])
                    index_j = reference_items.index(items[1])

                    # If the order is incorrect
                    if index_j < index_i:
                        metric += 2
                    else:
                        # If the order is correct
                        metric += 0

                else:
                    # If the order is irrelevant
                    metric += 1

                worst_case += 2

            metric /= worst_case
            ndpm[sequence_index] = metric

        return ndpm.mean()

    def diversity(self, recommender, metric):
        diversity = np.full(len(self.test_set), 0.0, dtype=float)

        for sequence_index, sequence in enumerate(self.test_set):
            recommended_sequence = recommender.recommend(sequence[0], self.k)
            recommended_items = self._get_item_list(recommended_sequence)

            for items in itertools.combinations(recommended_items, 2):
                diversity[sequence_index] += (1 - metric.similarity(items[0], items[1]))

            diversity[sequence_index] /= self.k * (self.k - 1) * 0.5

        return diversity.mean()

    def novelty(self, recommender):
        novelty = np.full(len(self.test_set), 0.0, dtype=float)

        for sequence_index, sequence in enumerate(self.test_set):
            recommended_sequence = recommender.recommend(sequence[0], self.k)
            recommended_items = self._get_item_list(recommended_sequence)
            metric = 0

            for item in recommended_items:
                item_index = self.items.index(item)
                item_distribution = self.distribution[item_index]

                # log(0) = 0 by definition
                if item_distribution != 0:
                    metric += math.log2(item_distribution)

            metric *= -1 * (1 / self.k)
            novelty[sequence_index] = metric

        return novelty.mean()

    def serendipity(self, recommender, primitive_k=None):
        primitive_recommender = baseline.MostPopularRecommender(self.training_set, self.items)
        primitive_sequence = primitive_recommender.recommend((0, 0, 0), self.k if primitive_k is None else primitive_k)
        primitive_items = self._get_item_list(primitive_sequence)

        serendipity = np.full(len(self.test_set), 0.0, dtype=float)

        for sequence_index, sequence in enumerate(self.test_set):
            local_k = min(self.k, len(sequence) - 1)
            hit = 0

            recommended_sequence = recommender.recommend(sequence[0], self.k)
            reference_items = self._get_item_list(sequence[1:])

            # For each rating in the recommended sequence
            for rating in recommended_sequence:
                # Check if the item is also in the primitive sequence
                if rating[0] in primitive_items:
                    continue

                # Check if the item is also in the reference path
                if rating[0] in reference_items:
                    # Only the first time
                    reference_items.remove(rating[0])
                    hit += 1

            serendipity[sequence_index] = hit / local_k

        return serendipity.mean()

    def confidence(self, recommender):
        confidence = np.full(len(self.test_set), 0.0, dtype=float)

        for sequence_index, sequence in enumerate(self.test_set):
            recommended_sequence = recommender.recommend(sequence[0], self.k)

            previous_rating = sequence[0]

            for rating in recommended_sequence:
                probability = recommender.predict_item(previous_rating, rating[0])
                confidence[sequence_index] += probability
                previous_rating = rating

            recommender.reset()

            # Mean for each sequence
            confidence[sequence_index] /= self.k

        return confidence.mean()

    def perplexity(self, recommender):
        cross_entropy = np.full(len(self.test_set), 0.0, dtype=float)
        count_ratings = 0

        for sequence_index, sequence in enumerate(self.test_set):

            for rating_index, rating in enumerate(sequence):
                try:
                    next_item = sequence[rating_index + 1][0]
                    probability = recommender.predict_item(rating, next_item)

                    if probability > 0:
                        # noinspection PyUnresolvedReferences
                        cross_entropy[sequence_index] -= np.log2(probability)
                    else:
                        cross_entropy[sequence_index] = math.inf

                    count_ratings += 1

                except IndexError:
                    # The sequence has ended
                    pass

            recommender.reset()

        perplexity = 2 ** (cross_entropy.sum() / count_ratings)

        return perplexity
