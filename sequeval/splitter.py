import random
from abc import ABC
from abc import abstractmethod


class Splitter(ABC):

    def __init__(self, test_ratio):
        if test_ratio < 0 or test_ratio > 1:
            raise ValueError('Test ratio must be a number between 0 and 1')
        self.test_ratio = test_ratio

    @abstractmethod
    def split(self, sequences):
        pass


class RandomSplitter(Splitter):

    def split(self, sequences):
        """
        Perform a random splitting according to the test ratio.

        :param sequences: A list of sequences.
        :return: A list of training and a list of test sequences.
        """
        training_set = []
        test_set = []

        # Randomize the sequences
        random_sequences = list(sequences)
        random.shuffle(random_sequences)

        # Target number of sequences in the training set
        target_training = len(random_sequences) * (1 - self.test_ratio)

        # Put the sequences in the test or training sets
        for counter, sequence in enumerate(random_sequences):
            if counter < target_training:
                training_set.append(sequence)
            else:
                test_set.append(sequence)

        return training_set, test_set


class TimestampSplitter(Splitter):

    def split(self, sequences):
        """
        Perform a timestamp splitting according to the test ratio.

        :param sequences: A list of sequences.
        :return: A list of training and a list of test sequences.
        """
        training_set = []
        test_set = []

        # The sequences must be ordered by timestamp
        ordered_sequences = list(sequences)
        sorted(ordered_sequences, key=lambda item: item[0][2])

        # Target number of sequences in the training set
        target_training = len(ordered_sequences) * (1 - self.test_ratio)

        # Put the sequences in the test or training sets
        for counter, sequence in enumerate(ordered_sequences):
            if counter < target_training:
                training_set.append(sequence)
            else:
                test_set.append(sequence)

        return training_set, test_set
