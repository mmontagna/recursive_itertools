import unittest

from recursive_itertools import *

class TestBase64Encoder(unittest.TestCase):

    def test_remove_object_on_list(self):
        self.assertEqual([1,2], rfilter([None, 1, None, 2], lambda x: x is not None))

    def test_remove_object_on_nested_list(self):
        self.assertEqual([1,2, [3,4]], rfilter([None, 1, None, 2, [None, 3, 4, None]], lambda x: x is not None))



    def test_remove_object_on_dictionary(self):
        self.assertEqual({'a': 1}, rfilter({'a': 1, 'b': None}, lambda x: x is not None))

    def test_remove_object_on_nested_dictionary(self):
        self.assertEqual({'a': {'c': 2}}, rfilter({'a': {'c': 2, 'd': None}, 'b': None}, lambda x: x is not None))




if __name__ == '__main__':
    unittest.main()