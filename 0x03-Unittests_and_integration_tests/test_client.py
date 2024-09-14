#!/usr/bin/env python3
'''module to test client.GithubOrgClient'''


import client
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
import unittest
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    '''class inheriting from unittest'''
    @parameterized.expand([
        ('google', {"login": "google"}),
        ('abc', {"login": "abc"})
    ])
    @patch('utils.get_json')  # patch to make sure getjson is called once
    def test_org(self, name, result, mock_get_json):
        '''tests that githuborgclient returns correct value'''
        mock_get_json.return_value = result

        client_github = GithubOrgClient(name)

        self.assertEqual(client_github.org(), result)

    @patch.object(client.GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos_url(self, mock_public_repos_property):
        '''tests public_repos_url, a method in class githuborgclient'''
        with patch('client.GithubOrgClient.org') as mock_github_org:
            '''patch githuborg making it return a known payload'''
            client_github = GithubOrgClient('google')
            mock_github_org.return_value = {'public_repos_url':
                                            'https://api.github.com'
                                            '/orgs/google/repos'}
            mock_public_repos_property.return_value = \
                'https://api.github.com/orgs/google/repos'

            self.assertEqual(client_github._public_repos_url,
                             'https://api.github.com/orgs/google/repos')


if __name__ == '__main__':
    unittest.main()
