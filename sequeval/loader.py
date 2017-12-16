from abc import ABC
from abc import abstractmethod

import pandas


class Loader(ABC):

    @abstractmethod
    def load(self, file):
        """
        Load a file containing ratings in a list of ratings.
        The list must be ordered by user and timestamp.

        :param file: The file path.
        :return: A list of ratings.
        """
        pass


class MovieLensLoader(Loader):

    def __init__(self, limit, skip):
        """
        :param limit: The limit between positive and negative ratings.
        :param skip: The number of rows to skip when reading the file.
        """
        self.limit = limit
        self.skip = skip

    def load(self, file):
        """
        Load a CSV file with a MovieLens-like format.
        Only the ratings higher than the limit will be considered.

        :param file: The file path.
        :return: A list of ratings.
        """
        # Read the input file
        df_input = pandas.read_csv(file, names=['userId', 'itemId', 'rating', 'timestamp'], skiprows=self.skip)

        # Select the ratings higher than the limit
        df_filtered = df_input.loc[df_input['rating'] > self.limit]

        # Sort the by user and timestamp
        df_sorted = df_filtered.sort_values(by=['userId', 'timestamp'])

        # Create a list of ratings
        ratings = []
        for row in df_sorted.itertuples():
            # itemId, userId, timestamp
            ratings.append((row[2], row[1], row[4]))

        return ratings
