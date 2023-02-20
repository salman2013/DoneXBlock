from django.test.testcases import TestCase
from .utils import make_block, make_url
import json
from unittest.mock import patch
import requests


class TestDefaultDoneValue(TestCase):

    def setUp(self):
        super().setUp()

        self.xblock = make_block()

    def test_done_value(self):
        assert not self.xblock.done

    @patch('requests.post', return_value={'state': False})
    def test_post(self, mock_post):
        info = {"done": False}
        url = make_url()
        resp = requests.post(url, data=json.dumps(
            info), headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with(url, data=json.dumps(
            info), headers={'Content-Type': 'application/json'})
        assert resp['state'] is False
