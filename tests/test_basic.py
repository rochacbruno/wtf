import os
import sys
import unittest
from wtf.news_app import create_app
from flask import request

sys.path.append(os.path.abspath(__name__))


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_filename="settings.py")

    def test_request_args(self):
        with self.app.test_request_context('/?name=BrunoRocha'):
             self.assertEqual(request.args.get('name'), 'BrunoRocha')