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

    def test_instance(self):
        """Checks if an instance of State is created"""
        state = State()
        state1 = State()
        self.assertNotEqual(state.id, state1.id)
        self.assertNotEqual(state.created_at, state1.created_at)
        self.assertNotEqual(state.updated_at, state1.updated_at)
        self.assertIn(state, storage.all().values())
        self.assertIn(st1ate, storage.all().values())
        self.assertEqual(State.name, "")

    def test_attr(self):
        """Checks if the attributes are correct"""
        my_state = State()
        self.assertEqual(my_state.name, "")


if __name__ == '__main__':
    unittest.main()
