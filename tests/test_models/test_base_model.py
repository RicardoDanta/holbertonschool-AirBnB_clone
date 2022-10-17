#!/usr/bin/python3
"""Test of BaseModel"""

import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def test_save(self):
        """Checking Save"""
        basemodel = BaseModel()
        basemodel.save()
        self.assertNotEqual(basemodel.created_at, basemodel.updated_at)

    def test_basemodel_to_dict(self):
        """Check BaseModel to_dict"""
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(basemodel_dict["__class__"], "BaseModel")
        self.assertEqual(type(basemodel_dict["created_at"]), str)
        self.assertEqual(type(basemodel_dict["updated_at"]), str)
        self.assertEqual(basemodel_dict["id"], basemodel.id)
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test__str__(self):
        """Checks __str__"""
        basemodel = BaseModel()
        self.assertEqual(
            f"[{type(basemodel).__name__}] \
                ({basemodel.id}) {basemodel.__dict__}", str(basemodel))


if __name__ == '__main__':
    unittest.main()
