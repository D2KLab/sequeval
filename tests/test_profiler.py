import unittest

import sequeval
from .test_builder import sequences


class ProfilerTestSuite(unittest.TestCase):

    def test_users(self):
        profiler = sequeval.Profiler(sequences)
        self.assertEqual(2, profiler.users())

    def test_items(self):
        profiler = sequeval.Profiler(sequences)
        self.assertEqual(3, profiler.items())

    def test_ratings(self):
        profiler = sequeval.Profiler(sequences)
        self.assertEqual(8, profiler.ratings())

    def test_sequences(self):
        profiler = sequeval.Profiler(sequences)
        self.assertEqual(3, profiler.sequences())

    def test_sparsity(self):
        profiler = sequeval.Profiler(sequences)
        self.assertAlmostEqual(8 / 9, profiler.sparsity())

    def test_sequence_length(self):
        profiler = sequeval.Profiler(sequences)
        self.assertAlmostEqual(8 / 3, profiler.sequence_length())


if __name__ == '__main__':
    unittest.main()
