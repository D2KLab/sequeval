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

You can test sequeval by running `pytest tests`. You can also compute the coverage of the tests with `pytest --cov sequeval`. These commands require, respectively, [pytest](https://pytest.org/) and [pytest-cov](https://github.com/pytest-dev/pytest-cov).

## Usage

You can try sequeval by running the script `python main.py`. For further information about the possible parameters, you can execute `python main.py -h`.

If you want to try the framework with the sample Yes.com dataset, you can run the following command:

```bash
python main.py --seed 1 --item_ratings 50 --random --delta "1000 s" datasets/yes_reduced.csv
```

The file `yes_reduced.csv` contains a random sample of the [Yes.com](http://web.archive.org/web/20170629232107/https://www.cs.cornell.edu/~shuochen/lme/data_page.html) dataset, reduced 10 times its original size. Please note that the Yes.com dataset was originally released under the terms of the [Creative Commons BY-NC-ND 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/) license.