import unittest

import sequeval
from .test_loader import ratings

sequences = [[(1, 1, 0), (2, 1, 5), (1, 1, 10)],
             [(3, 1, 30), (2, 1, 35)],
             [(1, 2, 30), (2, 2, 35), (2, 2, 40)]]

items = [1, 2, 3]


class BuilderTestSuite(unittest.TestCase):

    def test_builder(self):
        builder = sequeval.Builder(10)
        actual_sequences, actual_items = builder.build(ratings)
        self.assertEqual(sequences, actual_sequences)
        self.assertEqual(items, actual_items)


if __name__ == '__main__':
    unittest.main()
