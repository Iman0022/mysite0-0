import unittest
from . import function

class TestStringMethods(unittest.TestCase):

    def test_is_great_length(self):
        ans = function.is_great_length("Surprise Shawty!")
        self.assertEqual(ans, True)