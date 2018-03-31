#!/usr/bin/env python

# try:
from setuptools import setup, find_packages
# except ImportError:
    # from distutils.core import setup


def readme():
    with open('README.md') as f:
        return f.read()

config = {
    'name': 'sinkhorn_knopp',
    'version': '0.2',
    'description': 'Sinkhorn-Knopp Algorithm',
    'long_description': readme(),
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    'license': 'MIT',
    'url': 'https://github.com/btaba/sinkhorn_knopp',
    'author': 'Baruch Tabanpour',
    'author_email': 'baruch@tabanpour.info',
    'license': 'MIT',
    'packages': find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    'install_requires': [
        'numpy>=1'
    ],
    'zip_safe': False,
    'test_suite': 'nose.collector',
    'tests_require': ['nose'],
    'keywords': [
        'sinkhorn-knopp',
        'doubly stochastic matrix'
    ]
}

setup(**config)
