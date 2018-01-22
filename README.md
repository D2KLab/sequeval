# Sequeval
Sequeval is an offline evaluation framework for sequence-based recommender systems developed in Python.

## Dependencies

Sequeval requires [numpy](http://www.numpy.org/), [scipy](http://www.scipy.org/), [pandas](http://pandas.pydata.org/), and [matplotlib](http://matplotlib.org/).

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

You can test sequeval by running `pytest tests`. You can also compute the coverage of the tests with `pytest --cov tests`. These commands require, respectively, [pytest](https://pytest.org/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov).