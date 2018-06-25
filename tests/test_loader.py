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

    def test_uirt(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.UIRTLoader()
        self.assertEqual(ratings, loader.load(io.StringIO(fake_input)))

    def test_uirt_ordering(self):
        fake_input = "1,2,5,5\n1,1,5,0\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.UIRTLoader()
        self.assertEqual(ratings, loader.load(io.StringIO(fake_input)))

    def test_uirt_user_ratings(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.UIRTLoader(user_ratings=5)
        self.assertEqual(ratings[:5], loader.load(io.StringIO(fake_input)))

    def test_uirt_item_ratings(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.UIRTLoader(item_ratings=2)
        self.assertEqual(ratings[:3] + ratings[4:], loader.load(io.StringIO(fake_input)))

    def test_uirt_threshold(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,2,40"
        loader = sequeval.UIRTLoader(threshold=3)
        self.assertEqual(ratings[0:8], loader.load(io.StringIO(fake_input)))

    def test_uirt_skip(self):
        fake_input = "1,1,5,0\n1,2,5,5\n1,1,5,10\n1,3,5,30\n1,2,5,35,\n2,1,5,5\n2,1,5,30\n2,2,5,35\n2,2,5,40"
        loader = sequeval.UIRTLoader(skip=1)
        self.assertEqual(ratings[1:], loader.load(io.StringIO(fake_input)))


if __name__ == '__main__':
    unittest.main()
