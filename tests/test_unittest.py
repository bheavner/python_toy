# -*- coding: utf-8 -*-
"""A unit testing module for python_toy"""

import unittest

class ToyTests(unittest.TestCase):
    """Toy Unit Test."""

    def test_foo(self):
        """Double check that unittest is working."""
        self.assertTrue(isinstance('abc', str))

def main():
    """Run the unit tests"""
    unittest.main()

if __name__ == '__main__':
    main()
