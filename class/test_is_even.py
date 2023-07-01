import unittest
from . import function

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        ans = function.is_even(6)
        self.assertEqual(ans, "Even")
        