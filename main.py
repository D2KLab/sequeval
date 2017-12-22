import argparse

import pytimeparse

import sequeval
import sequeval.baseline as baseline


def evaluation(compute, recommender, similarity):
    print("%10s\t" % recommender.name, end='')
    print("%10f\t" % compute.coverage(recommender), end='')
    print("%10f\t" % compute.precision(recommender), end='')
    print("%10f\t" % compute.ndpm(recommender), end='')
    print("%10f\t" % compute.diversity(recommender, similarity), end='')
    print("%10f\t" % compute.novelty(recommender), end='')
    print("%10f\t" % compute.serendipity(recommender), end='')
    print("%10f\t" % compute.confidence(recommender), end='')
    print("%10f" % compute.perplexity(recommender))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='An evaluation framework for sequence-based recommender systems.')

    parser.add_argument('file', type=str, help='file containing the ratings')
    parser.add_argument('--ratings', type=int, default=20, help='minimum number of ratings per user')
    parser.add_argument('--delta', type=str, default='8 hours', help='time interval to create the sequences')
    parser.add_argument('--random', action='store_true', default=False, help='use random instead of timestamp splitter')
    parser.add_argument('--ratio', type=float, default=0.2, help='percentage of sequences in the test set')
    parser.add_argument('--k', type=int, default=5, help='length of the recommended sequences')

    args = parser.parse_args()

    loader = sequeval.MovieLensLoader(min_ratings=args.ratings)
    ratings = loader.load(args.file)

    builder = sequeval.Builder(pytimeparse.parse(args.delta))
    sequences, items = builder.build(ratings)

    print("# Profiler")
    profiler = sequeval.Profiler(sequences)
    print("Users:", profiler.users())
    print("Items:", profiler.items())
    print("Ratings:", profiler.ratings())
    print("Sequences:", profiler.sequences())
    print("Sparsity:", profiler.sparsity())
    print("Length:", profiler.sequence_length())

    if args.random is True:
        print("\n# Random splitter")
        splitter = sequeval.RandomSplitter(args.ratio)
    else:
        print("\n# Timestamp splitter")
        splitter = sequeval.TimestampSplitter(args.ratio)
    training_set, test_set = splitter.split(sequences)
    print("Training set:", len(training_set))
    print("Test set:", len(test_set))

    print("\n# Evaluator")
    print("%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s" %
          ("Algorithm", "Coverage", "Precision", "nDPM", "Diversity",
           "Novelty", "Serendipity", "Confidence", "Perplexity"))
    evaluator = sequeval.Evaluator(training_set, test_set, items, args.k)
    cosine = sequeval.CosineSimilarity(training_set, items)

    most_popular = baseline.MostPopularRecommender(training_set, items)
    evaluation(evaluator, most_popular, cosine)

    random = baseline.RandomRecommender(training_set, items)
    evaluation(evaluator, random, cosine)

    unigram = baseline.UnigramRecommender(training_set, items)
    evaluation(evaluator, unigram, cosine)

    bigram = baseline.BigramRecommender(training_set, items)
    evaluation(evaluator, bigram, cosine)
