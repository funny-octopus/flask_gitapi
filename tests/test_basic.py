import os
import sys
import unittest
from app import create_app
from config import TestConfig


USERNAME = 'home-assistant'
REPO = 'home-assistant'


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def test_wrong_url(self):
        response = self.client.get('/wrong/url')
        self.assertIn(b'Not Found Error', response.data)
        self.assertEqual(response.status_code, 404)

    def test_wrong_method(self):
        response = self.client.put('/repos/{USERNAME}/{REPO}')
        self.assertIn(b'Method Not Allowed', response.data)
        self.assertEqual(response.status_code, 405)

    def test_details(self):
        response = self.client.get(f'/repos/{USERNAME}/{REPO}')
        self.assertIn(b'\"status\":\"ok\"', response.data)
        self.assertEqual(response.status_code, 200)

    def test_pulls(self):
        response = self.client.get(f'/repos/{USERNAME}/{REPO}/pulls')
        self.assertIn(b'\"status\":\"ok\"', response.data)
        self.assertEqual(response.status_code, 200)

    def test_issues(self):
        response = self.client.get(f'/repos/{USERNAME}/{REPO}/issues')
        self.assertIn(b'\"status\":\"ok\"', response.data)
        self.assertEqual(response.status_code, 200)

    def test_forks(self):
        response = self.client.get(f'/repos/{USERNAME}/{REPO}/forks')
        self.assertIn(b'\"status\":\"ok\"', response.data)
        self.assertEqual(response.status_code, 200)


# if __name__ == '__main__':
#     unittest.main()
#    

