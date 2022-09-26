from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
      '''runs before everything else'''
      self.client = app.test_client()
      app.config['TESTING'] = True

    def test_home_page(self):
      '''checks if home route loads'''
      with self.client:
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('board', session)

    def test_invalid_word(self):
      '''checks if server is active'''
      self.client.get('/')
      response = self.client.get('/check-word?word=thing')
      self.assertEqual(response.json['result'], 'not-on-board')
