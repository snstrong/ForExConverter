from unittest import TestCase
from app import app
# from flask import session
"""Tests for Flask app.py in ForExConverter project"""

from converter import Converter

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    def setUp(self):
        """Runs before every test."""
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_homepage(self):
        """Make sure HTML is displayed"""
        with self.client as client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<form action="/result" method="GET">', response.data)

    def test_results_page(self):
        """Test if result page displays correctly"""
        with self.client as client:
            response = client.get('/result?convert-from=USD&convert-to=USD&amount=1')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<table class="table table-borderless">',response.data)

    def test_invalid_input(self):
        """Test invalid input to make sure it redirects and displays error message"""
        with self.client as client:
            response = client.get('/result?convert-from=XX&convert-to=YY&amount=1', follow_redirects = True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Invalid currency code: XX',response.data)