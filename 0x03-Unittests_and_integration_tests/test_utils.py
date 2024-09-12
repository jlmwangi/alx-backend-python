#!/usr/bin/env python3
'''a unittest for utils.access_nested_map'''


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''a class that inherits from unittest testcase module'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''test access nested map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, KeyError):
        '''use assert raises to test that a keyerror is raised'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
