#!/usr/bin/env python3
'''a unittest for utils.access_nested_map'''


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, MagicMock, PropertyMock


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


class TestGetJson(unittest.TestCase):
    '''a class meant to test the get_json function'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')  # patching requests.get to return a mock response
    def test_get_json(self, test_url, test_payload, mock_get_json):
        '''method to test the get_json function'''
        mock_response = MagicMock()  # a response object with a json method
        mock_response.json.return_value = test_payload

        '''set return value of requests.get to mock_response'''
        mock_get_json.return_value = mock_response

        '''call the get_json method: method being tested'''
        result = get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''class to test memoize function'''

    def test_memoize(self):
        ''''test_memoize method'''

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', new_callable=MagicMock) as mock_a_method:

            mock_a_method.return_value = 42  # mock a_method to return a val
            obj = TestClass()

            '''access the property twice'''
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
