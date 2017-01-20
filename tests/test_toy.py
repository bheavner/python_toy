"""Testing the toy hello world method """

import unittest
import toy

class UnitTestTests(unittest.TestCase):
    """Test Unit Test."""

    def test_matches(self):
        """toy.hello_func() should return 'Hello!'"""
        self.assertTrue(toy.hello_func() == 'Hello!')

if __name__ == '__main__':
    unittest.main()
