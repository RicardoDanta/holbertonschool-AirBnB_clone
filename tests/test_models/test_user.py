#!/usr/bin/python3
"""Test User"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """User"""

    def test_instance(self):
        """Instance"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertTrue(isinstance(user, BaseModel))


if __name__ == '__main__':
    unittest.main()
