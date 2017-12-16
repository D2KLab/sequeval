import unittest

import sequeval
from .test_builder import sequences


class SplitterTestSuite(unittest.TestCase):

    def test_random_splitter(self):
        splitter = sequeval.RandomSplitter(0.4)
        training_set, test_test = splitter.split(sequences)
        self.assertEqual(2, len(training_set))
        self.assertEqual(1, len(test_test))

    def test_timestamp_splitter(self):
        splitter = sequeval.TimestampSplitter(0.4)
        training_set, test_test = splitter.split(sequences)
        self.assertEqual(sequences[:2], training_set)
        self.assertEqual(sequences[2:], test_test)


if __name__ == '__main__':
    unittest.main()
