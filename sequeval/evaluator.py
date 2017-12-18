import numpy as np


class Evaluator:

    def __init__(self, training_set, test_set, items, k):
        self.training_set = training_set
        self.test_set = test_set
        self.items = items
        self.k = k

        # Create the set of users
        users = []

        for sequence in training_set + test_set:
            for rating in sequence:
                users.append(rating)

        self.users = sorted(list(set(users)))

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
