from setuptools import setup

setup(
    name='sequeval',
    version='1.2.0',
    packages=['sequeval',
              'sequeval.baseline'],
    url='https://github.com/D2KLab/sequeval',
    license='MIT',
    author='Diego Monti',
    author_email='diego.monti@polito.it',
    description='An offline evaluation framework for sequence-based recommender systems',
    install_requires=['numpy',
                      'pandas',
                      'pytimeparse',
                      'scipy']
)
