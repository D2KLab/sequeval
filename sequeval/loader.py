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
        :rtype: Iterable.
        """
        pass


class MovieLensLoader(Loader):

    def __init__(self, user_ratings=0, item_ratings=0, threshold=None, skip=0):
        """
        :param user_ratings: The minimum number of ratings per each user.
        :param item_ratings: The minimum number of ratings per each item.
        :param threshold: The threshold between positive and negative ratings.
        :param skip: The number of rows to skip when reading the file.
        """
        self.user_ratings = user_ratings
        self.item_ratings = item_ratings
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

        if self.user_ratings > 0:
            # Count the ratings per each user
            df_users_counter = df_filtered.groupby(['userId']).size().reset_index(name='counter')

            # Select the users with more ratings than the minimum value
            good_users = df_users_counter.loc[df_users_counter['counter'] >= self.user_ratings]['userId']

            # Keep only the ratings associated with good users
            df_user_ratings = df_filtered.loc[df_filtered['userId'].isin(good_users)]
        else:
            df_user_ratings = df_filtered

        if self.item_ratings > 0:
            # Count the ratings per each item
            df_items_counter = df_user_ratings.groupby(['itemId']).size().reset_index(name='counter')

            # Select the items with more ratings than the minimum value
            good_items = df_items_counter.loc[df_items_counter['counter'] >= self.item_ratings]['itemId']

            # Keep only the ratings associated with good items
            df_item_ratings = df_user_ratings.loc[df_user_ratings['itemId'].isin(good_items)]
        else:
            df_item_ratings = df_user_ratings

        # Sort the by user and timestamp
        df_sorted = df_item_ratings.sort_values(by=['userId', 'timestamp'])

        # Create a list of ratings
        ratings = []
        for row in df_sorted.itertuples():
            # itemId, userId, timestamp
            ratings.append((row[2], row[1], int(row[4])))

        return ratings
