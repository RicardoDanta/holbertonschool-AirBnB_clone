#!/usr/bin/python3
"""Test Amenity"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8


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

    def test_pycodestyle(self):
        """Check Pycodestyle"""
        style = pep8.StyleGuide(quit=True)
        pycodestyle = style.check_files(['models/amenity.py'])
        self.assertEqual(pycodestyle.total_errors, 0, "fix pep8")

    def test_doc(self):
        """Check docstring"""
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
