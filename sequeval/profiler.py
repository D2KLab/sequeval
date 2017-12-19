class Profiler:

    def __init__(self, sequences):
        users = []
        items = []
        ratings = []

        for sequence in sequences:
            for rating in sequence:
                users.append(rating[1])
                items.append(rating[0])
                ratings.append(rating)

        self._sequences = sequences
        self._users = list(set(users))
        self._items = list(set(items))
        self._ratings = ratings

    def users(self):
        """
        :return: The number of unique users.
        """
        return len(self._users)

    def items(self):
        """
        :return: The number of unique items.
        """
        return len(self._items)

    def ratings(self):
        """
        :return: The number of ratings.
        """
        return len(self._ratings)

    def sequences(self):
        """
        :return: The number of sequences.
        """
        return len(self._sequences)

    def sparsity(self):
        """
        Compute the sequence-item sparsity, that is the number of ratings
        divided by the number of sequences times the number of items.

        :return: The sequence-item sparsity.
        """
        return self.ratings() / (self.sequences() * self.items())

    def sequence_length(self):
        """
        :return: The average length of a sequence.
        """
        return self.ratings() / self.sequences()
