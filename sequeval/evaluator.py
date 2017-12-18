import itertools

import numpy as np


class Evaluator:

    def __init__(self, training_set, test_set, items, k):
        self.training_set = training_set
        self.test_set = test_set
        self.items = items
        self.k = k
        self.users = self._get_user_set(training_set + test_set)

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

    def coverage(self, recommender):
        total_items = 0

        for user in self.users:
            recommended_items = []

            for item in self.items:
                seed_rating = (item, user, 0)
                recommended_sequence = recommender.generate(seed_rating, self.k)

                for rating in recommended_sequence:
                    recommended_items.append(rating[0])

            total_items += len(set(recommended_items))

        coverage = total_items / (len(self.items) * len(self.users))

        return coverage

    def precision(self, recommender):
        precision = np.full(len(self.test_set), 0.0, dtype=float)

        # For each sequence in the test set
        for sequence_index, sequence in enumerate(self.test_set):
            local_k = min(self.k, len(sequence) - 1)
            hit = 0

            recommended_sequence = recommender.generate(sequence[0], self.k)

            # Create a list of reference items
            reference_items = []

            for rating in sequence[1:]:
                reference_items.append(rating[0])

            # For each rating in the recommended sequence
            for rating in recommended_sequence:
                # Check if it is also in the reference path
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
            recommended_sequence = recommender.generate(sequence[0], self.k)
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
