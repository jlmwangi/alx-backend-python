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
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('utils.get_json')  # patch to make sure getjson is called once
    def test_org(self, name, expected_url, mock_get_json):
        '''tests that githuborgclient returns correct value'''
        client_github = GithubOrgClient(name)

        mock_get_json.return_value = {'orgs': expected_url}

        self.assertEqual(client_github.org(),
                         'https://api.github.com/orgs/google')

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

    @patch('utils.get_json')
    def test_public_repos(self, mock_get_json):
        '''mock get_json to get a payload of your choice'''
        client_github = GithubOrgClient('google')
        mock_get_json.return_value = [
                {'name': 'repo1'},
                {'name': 'repo2'}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            '''mck public repos_url to return repos'''
            mock_public_repos_url.return_value = \
                'https://api.github.com/orgs/google/repos'

            repos = client_github.public_repos()

            self.assertEqual(repos, ['repo1', 'repo2'])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with('https://api.github.com/\
                    orgs/google/repos')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "my_license"}}, "my_license", True)
    ])
    def test_has_license(self, repo, license_key, expected_val):
        '''test has_license method'''
        client_github = GithubOrgClient('google')

        result = client_github.has_license(repo, license_key)
        self.assertEqual(result, expected_val)


if __name__ == '__main__':
    unittest.main()
