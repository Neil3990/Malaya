import setuptools


__packagename__ = 'malaya-gpu'

setuptools.setup(
    name = __packagename__,
    packages = setuptools.find_packages(),
    version = '1.9.3',
    python_requires = '>=3.6.*',
    description = 'Natural-Language-Toolkit for bahasa Malaysia, powered by Deep Learning. GPU Version',
    author = 'huseinzol05',
    author_email = 'husein.zol05@gmail.com',
    url = 'https://github.com/huseinzol05/Malaya',
    download_url = 'https://github.com/huseinzol05/Malaya/archive/master.zip',
    keywords = ['nlp', 'bm'],
    install_requires = [
        'xgboost==0.80',
        'sklearn',
        'sklearn_crfsuite',
        'scikit-learn==0.19.1',
        'requests',
        'fuzzywuzzy',
        'tqdm',
        'unidecode',
        'tensorflow-gpu',
        'numpy',
        'scipy',
        'python-levenshtein',
        'PySastrawi',
        'toolz',
    ],
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing',
    ],
    long_description = open('readme-pypi.rst').read(),
)
