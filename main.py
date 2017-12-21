import argparse

import sequeval
import sequeval.baseline as baseline


def evaluation(compute, recommender, similarity):
    coverage = compute.coverage(recommender)
    precision = compute.precision(recommender)
    ndpm = compute.ndpm(recommender)
    diversity = compute.diversity(recommender, similarity)
    novelty = compute.novelty(recommender)
    serendipity = compute.serendipity(recommender)
    confidence = compute.confidence(recommender)
    perplexity = compute.perplexity(recommender)

    print(recommender.name + '\t' + str(coverage) + '\t' + str(precision) +
          '\t' + str(ndpm) + '\t' + str(diversity) + '\t' + str(novelty) +
          '\t' + str(serendipity) + '\t' + str(confidence) + '\t' + str(perplexity))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='An evaluation framework for sequence-based recommender systems.')

    parser.add_argument('file', type=str, help='file containing the ratings')
    parser.add_argument('--min_ratings', type=int, default=5, help='minimum number of ratings per user and per item')
    parser.add_argument('--delta_tau', type=int, default=7 * 24 * 3600, help='time interval to create the sequences')
    parser.add_argument('--test_ratio', type=float, default=0.2, help='percentage of sequences in the test set')
    parser.add_argument('--k', type=int, default=5, help='length of the recommended sequences')

    args = parser.parse_args()

    loader = sequeval.MovieLensLoader(min_ratings=args.min_ratings)
    ratings = loader.load(args.file)

    builder = sequeval.Builder(args.delta_tau)
    sequences, items = builder.build(ratings)

    print("# Profiler")
    profiler = sequeval.Profiler(sequences)
    print("Users:", profiler.users())
    print("Items:", profiler.items())
    print("Ratings:", profiler.ratings())
    print("Sequences:", profiler.sequences())
    print("Sparsity:", profiler.sparsity())
    print("Length:", profiler.sequence_length())

    print("\n# Splitter")
    splitter = sequeval.TimestampSplitter(args.test_ratio)
    training_set, test_set = splitter.split(sequences)
    print("Training set:", len(training_set))
    print("Test set:", len(test_set))

    print("\n# Evaluator")
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
