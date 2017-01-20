# -*- coding: utf-7 -*-
"""An example setup.py"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIG = {
    'description': 'My Toy Python Project',
    'author': 'Ben Heavner',
    'url': 'https://github.com/bheavner/python_toy',
    'download_url': 'https://github.com/bheavner/python_toy',
    'author_email': 'bheavner@gmail.com',
    'version': '0.1.0.dev1',
    'install_requires': [],
    'packages': ['toy'],
    'scripts': [],
    'name': 'python_toy'
}

setup(**CONFIG)
