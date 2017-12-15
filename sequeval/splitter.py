from abc import ABC
from abc import abstractmethod


class Splitter(ABC):

    def __init__(self, test_ratio):
        self.test_ratio = test_ratio

    @abstractmethod
    def split(self, sequences):
        pass


class RandomSplitter(Splitter):

    def split(self, sequences):
        # TODO
        return sequences, sequences


class TimestampSplitter(Splitter):

    def split(self, sequences):
        # TODO
        return sequences, sequences
