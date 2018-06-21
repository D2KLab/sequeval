from flask import Flask, render_template, json, request

import sequeval
import sequeval.baseline as baseline

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


def parse(value):
    if value == float('inf'):
        return 'Infinite'
    if isinstance(value, float):
        return str("%.4f" % round(value, 4))
    return str(value)


def evaluation(compute, recommender, similarity):
    return [recommender.name,
            parse(compute.coverage(recommender)),
            parse(compute.precision(recommender)),
            parse(compute.ndpm(recommender)),
            parse(compute.diversity(recommender, similarity)),
            parse(compute.novelty(recommender)),
            parse(compute.serendipity(recommender)),
            parse(compute.confidence(recommender)),
            parse(compute.perplexity(recommender))]


@app.route("/run", methods=['GET'])
def run():
    _user_ratings = int(request.args.get('user-ratings'))
    _item_ratings = int(request.args.get('item-ratings'))
    _splitter = request.args.get('splitter')
    _ratio = float(request.args.get('ratio')) / 100
    _k = int(request.args.get('length'))

    loader = sequeval.MovieLensLoader(user_ratings=_user_ratings, item_ratings=_item_ratings)
    ratings = loader.load('datasets/yes_reduced.csv')

    builder = sequeval.Builder('1000 s')
    sequences, items = builder.build(ratings)

    profiler = sequeval.Profiler(sequences)
    response = {'profiler': {'users': profiler.users(),
                             'items': profiler.items(),
                             'ratings': profiler.ratings(),
                             'sequences': profiler.sequences(),
                             'sparsity': parse(profiler.sparsity()),
                             'length': parse(profiler.sequence_length())}}

    if _splitter == 'random':
        splitter = sequeval.RandomSplitter(_ratio)
    else:
        splitter = sequeval.TimestampSplitter(_ratio)
    training_set, test_set = splitter.split(sequences)
    response['splitter'] = {'training': len(training_set),
                            'test': len(test_set)}

    evaluator = sequeval.Evaluator(training_set, test_set, items, _k)
    cosine = sequeval.CosineSimilarity(training_set, items)

    response['evaluator'] = []

    most_popular = baseline.MostPopularRecommender(training_set, items)
    response['evaluator'].append(evaluation(evaluator, most_popular, cosine))

    random = baseline.RandomRecommender(training_set, items)
    response['evaluator'].append(evaluation(evaluator, random, cosine))

    unigram = baseline.UnigramRecommender(training_set, items)
    response['evaluator'].append(evaluation(evaluator, unigram, cosine))

    bigram = baseline.BigramRecommender(training_set, items)
    response['evaluator'].append(evaluation(evaluator, bigram, cosine))

    return json.dumps(response)


if __name__ == "__main__":
    app.run()
