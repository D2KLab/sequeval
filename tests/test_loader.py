import io
import unittest

import sequeval

ratings = [(1, 1, 0),
           (2, 1, 5),
           (1, 1, 10),
           (3, 1, 30),
           (2, 1, 35),
           (1, 2, 5),
           (1, 2, 30),
           (2, 2, 35),
           (2, 2, 40)]


class LoaderTestSuite(unittest.TestCase):

    def test_movielens(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.MovieLensLoader()
        self.assertEqual(ratings, loader.load(io.StringIO(fake_input)))

    def test_movielens_ordering(self):
        fake_input = "1,2,5,5\n1,1,5,0\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.MovieLensLoader()
        self.assertEqual(ratings, loader.load(io.StringIO(fake_input)))

    def test_movielens_min_ratings(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.MovieLensLoader(min_ratings=5)
        self.assertEqual(ratings[:5], loader.load(io.StringIO(fake_input)))

    def test_movielens_threshold(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,2,40"
        loader = sequeval.MovieLensLoader(threshold=3)
        self.assertEqual(ratings[0:8], loader.load(io.StringIO(fake_input)))

    def test_movielens_skip(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.MovieLensLoader(skip=1)
        self.assertEqual(ratings[1:], loader.load(io.StringIO(fake_input)))


if __name__ == '__main__':
    unittest.main()
