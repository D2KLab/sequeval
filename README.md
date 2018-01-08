# Sequeval
An evaluation framework for sequence-based recommender systems.

## Installation

* Clone the repository and change the working directory:

  ```bash
  $ git clone git@github.com:D2KLab/sequeval.git
  $ cd sequeval
  ```

* Create a virtual environment:

  ```bash
  $ pip install virtualenv
  $ virtualenv venv
  ```

* Activate it:

  ```bash
  $ source venv/bin/activate
  ```

* Install the requirements:

  ```bash
  $ pip install -r requirements.txt
  ```

* Optionally run the tests:

  ```bash
  $ pytest tests
  ```

* Create a source distribution:

  ```bash
  $ python setup.py sdist
  ```

An installation package will be created inside the `dist` directory. It can be installed in another virtual environment by the means of `pip install sequeval-*.tar.gz`.