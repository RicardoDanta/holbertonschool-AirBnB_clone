#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.base_models import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """User"""

    def test_instance(self):
        """Instance"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.passqord, "")
        self.assertEqual(user.first_name, "")
        self.assertEuqal(user.last_name, "")
        self.assertTrue(isinstance(user, BaseModel))

    def test_pep8(self):
        """Pycodestyle"""


if __name__ == '__main__':
    unittest.main()
