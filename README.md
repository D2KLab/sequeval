# Sequeval

[![Build Status](https://travis-ci.org/D2KLab/sequeval.svg?branch=master)](https://travis-ci.org/D2KLab/sequeval)
[![codecov](https://codecov.io/gh/D2KLab/sequeval/branch/master/graph/badge.svg)](https://codecov.io/gh/D2KLab/sequeval)

Sequeval is an offline evaluation framework for sequence-based recommender systems developed in Python.

## Architecture

The package `sequeval` is composed of the following modules:

- `loader.py`, which contains the code for reading the ratings from a file. The class *MovieLensLoader* extends the abstract class *Loader* and it deals with CSV files compliant with the [MovieLens](https://grouplens.org/datasets/movielens/) format;
- `builder.py`, which contains the class *Builder* that creates a list of sequences from the ratings;
- `profiler.py`, which contains the class *Profiler* that computes some statistics about the sequences;
- `splitter.py`, which contains the abstract class *Splitter* and the concrete classes *RandomSplitter* and *TimestampSplitter*;
- `recommender.py`, which contains the abstract class *Recommender* that needs to be implemented by any recommender relying on this framework;
- `evaluator.py`, which contains the class *Evaluator* that includes the methods for computing the metrics during the evaluation phase;
- `similarity.py`, which contains the abstract class *Similarity* and the concrete class *CosineSimilarity*;
- `indexlist.py`, which contains the class *IndexList* that extends *MutableSequence*.

The package `sequeval.baseline` includes the following baseline recommenders:

- `mostpopular.py`, which contains the class *MostPopularRecommender*;
- `random.py`, which contains the class *RandomRecommender*;
- `unigram.py`, which contains the class *UnigramRecommender*;
- `bigram.py`, which contains the class *BigramRecommender*.

## Dependencies

Sequeval requires [numpy](http://www.numpy.org/), [pandas](http://pandas.pydata.org/), [pytimeparse](https://github.com/wroberts/pytimeparse), and [scipy](http://www.scipy.org/).

## Installation

If you interesting in using sequeval in your own project, you can install it with `pip`:

```bash
$ pip install git+https://github.com/D2KLab/sequeval.git
```

If you want to run the sample script `main.py` you need to first clone the repository and then install the requirements:

```bash
$ pip install -r requirements.txt
```

## Testing

You can test sequeval by running `pytest tests`. You can also compute the coverage of the tests with `pytest --cov sequeval`. These commands require, respectively, [pytest](https://pytest.org/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov).

## Usage

You can try sequeval by running the script `python main.py`. For further information about the possible parameters, you can execute `python main.py -h`.

If you want to try the framework with the sample Yes.com dataset, you can run the following command:

```bash
python main.py --seed 1 --item_ratings 50 --random --delta "1000 s" datasets/yes_reduced.csv
```

The file `yes_reduced.csv` contains a random sample of the [Yes.com](http://web.archive.org/web/20170629232107/https://www.cs.cornell.edu/~shuochen/lme/data_page.html) dataset, reduced 10 times its original size. Please note that the Yes.com dataset was originally released under the terms of the [Creative Commons BY-NC-ND 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/) license.

## Team

- Diego Monti <diego.monti@polito.it>
- Enrico Palumbo <palumbo@ismb.it>
- Giuseppe Rizzo <giuseppe.rizzo@ismb.it>
- Maurizio Morisio <maurizio.morisio@polito.it>