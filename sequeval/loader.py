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

    def __init__(self, min_ratings=0, threshold=None, skip=0):
        """
        :param min_ratings: The minimum number of ratings per each user and per each item.
        :param threshold: The threshold between positive and negative ratings.
        :param skip: The number of rows to skip when reading the file.
        """
        self.min_ratings = min_ratings
        self.threshold = threshold
        self.skip = skip

    def load(self, file):
        """
        Load a CSV file with a MovieLens-like format.
        Only the ratings higher than the threshold will be considered.

        :param file: The file path.
        :return: A list of ratings.
        """
        # Read the input file
        df_input = pandas.read_csv(file, names=['userId', 'itemId', 'rating', 'timestamp'], skiprows=self.skip)

        # Select the ratings higher than the threshold
        if self.threshold is not None:
            df_filtered = df_input.loc[df_input['rating'] >= self.threshold]
        else:
            df_filtered = df_input

        if self.min_ratings > 0:
            # Count the ratings per each user
            df_users_counter = df_filtered.groupby(['userId']).size().reset_index(name='counter')

            # Select the users with more ratings than min_ratings
            users_min_ratings = df_users_counter.loc[df_users_counter['counter'] >= self.min_ratings]['userId']

            # Count the ratings per each item
            df_items_counter = df_filtered.groupby(['itemId']).size().reset_index(name='counter')

            # Select the items with more ratings than min_ratings
            items_min_ratings = df_items_counter.loc[df_items_counter['counter'] >= self.min_ratings]['itemId']

            # Keep only the ratings associated with frequent items and users
            df_min_ratings = df_filtered.loc[df_filtered['userId'].isin(users_min_ratings) &
                                             df_filtered['itemId'].isin(items_min_ratings)]
        else:
            df_min_ratings = df_filtered

        # Sort the by user and timestamp
        df_sorted = df_min_ratings.sort_values(by=['userId', 'timestamp'])

        # Create a list of ratings
        ratings = []
        for row in df_sorted.itertuples():
            # itemId, userId, timestamp
            ratings.append((row[2], row[1], int(row[4])))

        return ratings
