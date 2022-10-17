#!/usr/bin/python3
"""Test Amenity"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test"""

    def test_sub_class(self):
        """Sublcass"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """Instance"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == '__main__':
    unittest.main()
