import argparse
import random

import numpy as np

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
    print("%10.2f" % compute.perplexity(recommender))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sequeval: An offline evaluation framework for sequence-based RSs')

    parser.add_argument('file', type=str, help='file containing the ratings')
    parser.add_argument('--seed', type=int, default=None, help='seed for generating pseudo-random numbers')
    parser.add_argument('--user', type=int, default=0, help='minimum number of ratings per user')
    parser.add_argument('--item', type=int, default=0, help='minimum number of ratings per item')
    parser.add_argument('--delta', type=str, default='8 hours', help='time interval to create the sequences')
    parser.add_argument('--splitter', type=str, default='timestamp', help='dataset splitting protocol: '
                                                                          'random or timestamp')
    parser.add_argument('--ratio', type=float, default=0.2, help='percentage of sequences in the test set')
    parser.add_argument('--length', type=int, default=5, help='length of recommended sequences')

    args = parser.parse_args()

    print("\n# Parameters")
    print("File:", args.file)
    print("Seed:", args.seed)
    print("User ratings:", args.user)
    print("Item ratings:", args.item)
    print("Delta:", args.delta)
    print("Ratio:", args.ratio)
    print("Length:", args.length)

    # Set the random seed
    if args.seed is not None:
        random.seed(args.seed)
        np.random.seed(args.seed)

    loader = sequeval.UIRTLoader(user_ratings=args.user, item_ratings=args.item)
    ratings = loader.load(args.file)

    builder = sequeval.Builder(args.delta)
    sequences, items = builder.build(ratings)

    print("\n# Profiler")
    profiler = sequeval.Profiler(sequences)
    print("Users:", profiler.users())
    print("Items:", profiler.items())
    print("Ratings:", profiler.ratings())
    print("Sequences:", profiler.sequences())
    print("Sparsity:", profiler.sparsity())
    print("Length:", profiler.sequence_length())

    if args.splitter is 'random':
        print("\n# Random splitter")
        splitter = sequeval.RandomSplitter(args.ratio)
    elif args.splitter is 'timestamp':
        print("\n# Timestamp splitter")
        splitter = sequeval.TimestampSplitter(args.ratio)
    else:
        raise RuntimeError('Unknown splitter')
    training_set, test_set = splitter.split(sequences)
    print("Training set:", len(training_set))
    print("Test set:", len(test_set))

    print("\n# Evaluator")
    print("%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s" %
          ("Algorithm", "Coverage", "Precision", "nDPM", "Diversity",
           "Novelty", "Serendipity", "Confidence", "Perplexity"))
    evaluator = sequeval.Evaluator(training_set, test_set, items, args.length)
    cosine = sequeval.CosineSimilarity(training_set, items)

    most_popular = baseline.MostPopularRecommender(training_set, items)
    evaluation(evaluator, most_popular, cosine)

    random = baseline.RandomRecommender(training_set, items)
    evaluation(evaluator, random, cosine)

    unigram = baseline.UnigramRecommender(training_set, items)
    evaluation(evaluator, unigram, cosine)

    bigram = baseline.BigramRecommender(training_set, items)
    evaluation(evaluator, bigram, cosine)
