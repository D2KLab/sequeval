import unittest

import sequeval
from .test_loader import ratings

sequences = [[(1, 1, 0), (2, 1, 5), (1, 1, 10)],
             [(3, 1, 30), (2, 1, 35)],
             [(3, 2, 30), (2, 2, 35), (2, 2, 40)]]


class BuilderTestSuite(unittest.TestCase):

    def test_builder(self):
        builder = sequeval.Builder(10)
        self.assertEqual(sequences, builder.build(ratings))


if __name__ == '__main__':
    unittest.main()
