#!/usr/bin/env python3
'''module to test client.GithubOrgClient'''


import client
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
import unittest
from utils import get_json
#  from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

        mock_get_json.return_value = {'orgs': {'key': 'value'}}

        self.assertEqual(client_github.org(),
                         mock_get_json.return_value)

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


org_payload = {'id': 1, 'name': 'google-org'}
repos_payload = [{'name': 'repo1'}, {'name': 'repo2'}]
expected_repos = ['repo1', 'repo2']
apache2_repos = ['repo1']

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''test public repos method in an integration test'''
    @classmethod
    def setUpClass(cls):  # mock requests.get
        '''runs before all tests'''
        cls.get_patcher = patch('utils.get_json',
                                side_effect=cls.mock_get_json)
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''runs after all tests'''
        cls.get_patcher.stop()

    @staticmethod
    def mock_get_json(url):
        '''mock requests to return example payloads based on url'''
        if "orgs" in url:
            return TestIntegrationGithubOrgClient.org_payload
        elif "repos" in url:
            return TestIntegrationGithubOrgClient.repos_payload
        return {}


if __name__ == '__main__':
    unittest.main()
