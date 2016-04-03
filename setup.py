#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()

config = {
    'name': 'sinkhorn_knopp',
    'version': '0.1',
    'description': 'Sinkhorn-Knopp Algorithm',
    'long_description': readme(),
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    'license': 'MIT',
    'url': '',
    'author': 'Baruch Tabanpour',
    'author_email': 'baruch@tabanpour.info',
    'license': 'MIT',
    'packages': [],
    'install_requires': [
        'numpy'
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
