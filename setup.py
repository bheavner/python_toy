try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Toy Python Project',
    'author': 'Ben Heavner',
    'url': 'https://github.com/bheavner/python_toy',
    'download_url': 'https://github.com/bheavner/python_toy',
    'author_email': 'bheavner@gmail.com',
    'version': '0.1dev',
    'install_requires': [],
    'packages': ['Python Toy'],
    'scripts': [],
    'name': 'python_toy'
}

setup(**config)

