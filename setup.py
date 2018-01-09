from setuptools import setup

setup(
    name='sequeval',
    version='0.1.0',
    packages=['sequeval',
              'sequeval.baseline'],
    url='https://github.com/D2KLab/sequeval',
    license='MIT',
    author='Diego Monti',
    author_email='diego.monti@polito.it',
    description='An evaluation framework for sequence-based recommender systems',
    install_requires=['numpy',
                      'pandas',
                      'scipy']
)