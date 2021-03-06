import pytimeparse

from sequeval.indexlist import IndexList


class Builder:

    def __init__(self, interval):
        """
        :param interval: The time interval for creating the sequences.
        """
        if type(interval) is str:
            self.interval = pytimeparse.parse(interval)
        else:
            self.interval = interval

    def build(self, ratings):
        """
        Build a list of sequences and a list of unique items.
        Each sequence is a list of ratings.
        Each rating is a item, user, timestamp tuple.

        :param ratings: A list of ratings, ordered by user and timestamp.
        :return: A list of sequences, a list of unique items.
        """
        sequences = []

        s = None
        last_row = None

        # Each row is a rating
        for row in ratings:
            # This is the first rating available
            if last_row is None:
                last_row = row

            # We have found a new user
            elif last_row[1] != row[1]:
                last_row = row
                if s is not None:
                    sequences.append(s)
                    s = None

            # The new rating is part of the sequence
            elif row[2] < last_row[2] + self.interval:
                if s is None:
                    s = [last_row]
                s.append(row)
                last_row = row

            # The sequence has ended
            else:
                if s is not None:
                    sequences.append(s)
                    s = None
                last_row = row

        # The last possible sequence
        if s is not None:
            sequences.append(s)

        # Create the list of items
        items = IndexList()

        for sequence in sequences:
            for rating in sequence:
                items.append(rating[0])

        return sequences, items
