#!/usr/bin/python3
"""Test State"""

import unittest
import models
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):
    """State"""

    def test_subclass(self):
        """Checks if state is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state(self):
        """Checks if the attributes are correct"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
