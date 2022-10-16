#!/usr/bin/python3
"""Test Amenity"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8


class AmenityTest(unittest.TestCase):
    """Test"""

    def test_sub_class(self):
        """Sublcass"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_style(self):
        """Pycodestyle"""
        style = pep8.StyleGuide(quit=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instance(self):
        """Instance"""
        am = Amenity()
        self.assertEqual(am.name, "")
        self.assertTrue(isinstance(am, BaseModel))


if __name__ == '__main__':
    unittest.main()
