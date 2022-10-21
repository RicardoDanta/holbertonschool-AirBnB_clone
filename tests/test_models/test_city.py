#!/usr/bin/python3
"""Test City"""

import os
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test"""

    def test_attributes(self):
        """Attributes"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_instances(self):
        """Check if that instances are correct"""
        basemodel = BaseModel()
        self.assertIsInstance(basemodel, BaseModel)


if __name__ == '__main__':
    unittest.main()
