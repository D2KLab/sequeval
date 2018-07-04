import unittest

import sequeval

sequences = [[(1, 1, 0), (2, 1, 5), (1, 1, 10)],
             [(3, 1, 30), (2, 1, 35)],
             [(1, 2, 25), (2, 2, 35), (2, 2, 40)]]


class SplitterTestSuite(unittest.TestCase):

    def test_random_splitter(self):
        splitter = sequeval.RandomSplitter(0.4)
        training_set, test_test = splitter.split(sequences)
        self.assertEqual(2, len(training_set))
        self.assertEqual(1, len(test_test))

    def test_timestamp_splitter(self):
        splitter = sequeval.TimestampSplitter(0.4)
        training_set, test_test = splitter.split(sequences)
        self.assertEqual([sequences[0], sequences[2]], training_set)
        self.assertEqual([sequences[1]], test_test)


if __name__ == '__main__':
    unittest.main()
