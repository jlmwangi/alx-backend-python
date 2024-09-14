#!/usr/bin/env python3
'''module to test client.GithubOrgClient'''


from client import GithubOrgClient
from unittest.mock import patch, MagicMock
from parameterized import parameterized
import unittest
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    '''class inheriting from unittest'''
    @parameterized.expand([
        ('google', {"name": "google"}),
        ('abc', {"name": "abc"})
    ])
    @patch('utils.get_json')  # patch to make sure getjson is called once
    def test_org(self, name, result, mock_get_json):
        '''tests that githuborgclient returns correct value'''
        mock_get_json.return_value = result

        client_github = GithubOrgClient(name)

        self.assertEqual(client_github.org(), result)
