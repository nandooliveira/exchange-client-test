#! ../env/bin/python
# -*- coding: utf-8 -*-
u"""Modulo to test routes."""

import unittest
import requests
import json


class TextRoutes(unittest.TestCase):
    u"""TestCase to test routes of the API."""

    def setUp(self):
        u"""Setup test."""
        pass

    def test_home(self):
        """Test if the main route loads."""
        rv = requests.get('http://127.0.0.1:5000/api/v1')
        assert rv.status_code == 200
        assert is_json(rv.text)


def is_json(m_json):
    """Validate json."""
    try:
        json.loads(m_json)
    except ValueError:
        return False

    return True


if __name__ == '__main__':
    unittest.main()
