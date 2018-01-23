import unittest

import sequeval


class IndexListTestSuite(unittest.TestCase):

    def test_setitem(self):
        indexlist = sequeval.IndexList()
        indexlist.append(None)
        indexlist[0] = 'Zero'
        self.assertEqual(indexlist[0], 'Zero')
        self.assertEqual(indexlist.index('Zero'), 0)

    def test_append(self):
        indexlist = sequeval.IndexList()
        indexlist.append('Zero')
        indexlist.append('One')
        indexlist.append('Zero')
        self.assertEqual(indexlist[0], 'Zero')
        self.assertEqual(indexlist[1], 'One')
        self.assertEqual(indexlist.index('Zero'), 0)
        self.assertEqual(indexlist.index('One'), 1)

    def test_delete(self):
        indexlist = sequeval.IndexList()
        indexlist.append('Zero')
        del indexlist[0]
        self.assertEqual(indexlist[0], 'Zero')
        self.assertEqual(indexlist.index('Zero'), 0)

    def test_len(self):
        indexlist = sequeval.IndexList()
        indexlist.append('Zero')
        indexlist.append('One')
        indexlist.append('Zero')
        self.assertEqual(len(indexlist), 2)

    def test_insert(self):
        indexlist = sequeval.IndexList()
        indexlist.insert(1, 'Zero')
        self.assertEqual(indexlist[0], 'Zero')
        self.assertEqual(indexlist.index('Zero'), 0)


if __name__ == '__main__':
    unittest.main()
