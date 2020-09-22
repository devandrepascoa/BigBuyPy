import unittest
import os


class catalogTest(unittest.TestCase):

    def test_upper(self):
        api_key = os.environ.get('API_KEY', None)
        print(api_key)
        assert api_key is not None, "API_KEY not found"
