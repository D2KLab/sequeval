import collections


class IndexList(collections.MutableSequence):

    def __init__(self):
        """
        An IndexList is a list that efficiently stores the indexes associated to each value.
        Appending duplicate values is not allowed, in order to have unique indexes.
        """
        self._list = []
        self._index = {}

    def __setitem__(self, index, value):
        self._list.__setitem__(index, value)
        self._index[value] = index

    def __delitem__(self, index):
        # Not implemented
        pass

    def __getitem__(self, index):
        return self._list.__getitem__(index)

    def __len__(self):
        return self._list.__len__()

    def insert(self, index, value):
        self._list.insert(index, value)
        self._index[value] = self._list.index(value)

    def append(self, value):
        try:
            self._index[value]
        except KeyError:
            self._list.append(value)
            self._index[value] = len(self._list) - 1

    def index(self, value, start=0, stop=None):
        return self._index[value]
