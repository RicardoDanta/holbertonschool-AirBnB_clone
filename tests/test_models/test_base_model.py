#!/usr/bin/python3
""" Testing BaseModel """

import unittest
import os
from time import sleep
import models
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class test_basemodel(unittest.TestCase):
    """ Test BaseModel Class """

    def test_basemodel_save(self):
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

    def test_basemodel_to_dict_with_kwargs(self):
        """Check BaseModel to_dict with kwargs"""
        dict = {"name": "Holberton", "age": 89, "id": "0"}
        basemodel = BaseModel(**dict)
        self.assertEqual(basemodel.id, "0")
        self.assertEqual(basemodel.name, "Holberton")
        self.assertEqual(basemodel.age, 89)
        self.assertEqual(basemodel.__dict__, dict)

    def test_doc(self):
        """Checking BaseModel docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_datetime(self):
        """Check Datetime"""
        basemodel = BaseModel()
        self.assertIsInstance(basemodel.created_at, datetime)
        self.assertIsInstance(basemodel.updated_at, datetime)

    def test_id(self):
        """Check the id"""
        basemodel = BaseModel()
        basemodel2 = BaseModel()
        self.assertIsInstance(basemodel.id, str)
        self.assertNotEqual(basemodel.id, basemodel2.id)
        self.assertFalse(basemodel.id == basemodel2.id)

    def test_inst(self):
        """Check the instances of BaseModel"""
        basemodel = BaseModel()
        basemodel1 = BaseModel()
        self.assertNotEqual(basemodel.id, basemodel1.id)
        self.assertNotEqual(basemodel.created_at, basemodel1.created_at)
        self.assertNotEqual(basemodel.updated_at, basemodel1.updated_at)
        self.assertIn(basemodel, storage.all().values())
        self.assertIn(basemodel1, storage.all().values())

    def test_attr(self):
        """Checks Attributes"""
        basemodel = BaseModel()
        basemodel.name = "Holberton"
        basemodel.age = 89
        self.assertIs(datetime, type(basemodel.updated_at))
        self.assertIs(datetime, type(basemodel.created_at))
        self.assertIs(str, type(basemodel.id))
        self.assertEqual(int, type(basemodel.age))
        self.assertIn(basemodel.name, basemodel.to_dict().values())

    def test__str__(self):
        """Checks __str__"""
        basemodel = BaseModel()
        self.assertEqual(
            f"[{type(bm).__name__}] ({bm.id}) {bm.__dict__}", str(basemodel))

    def test_save(self):
        """Checks Save"""
        basemodel = BaseModel()
        updated_at = basemodel.__dict__['updated_at']
        basemodel.save()
        self.assertNotEqual(basemodel.__dict__['updated_at'], updated_at)
        self.assertTrue(os.path.isfile('file.json'))
        new_updated_at = basemodel.__dict__['updated_at']
        storage.reload()
        self.assertEqual(basemodel.__dict__['updated_at'], new_updated_at)
        basemodel1 = BaseModel()
        updated_at = basemodel1.__dict__['updated_at']
        basemodel1.save()
        self.assertNotEqual(basemodel1.__dict__['updated_at'], updated_at)
        self.assertTrue(os.path.isfile('file.json'))
        new_updated_at = basemodel1.__dict__['updated_at']
        storage.reload()
        self.assertEqual(basemodel1.__dict__['updated_at'], new_updated_at)

    def test_to_dict(self):
        """Checks to_dict"""
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(basemodel_dict["id"], basemodel.id)
        self.assertEqual(basemodel_dict["created_at"], basemodel.created_at.isoformat())
        self.assertEqual(basemodel_dict["updated_at"], basemodel.updated_at.isoformat())
        self.assertEqual(basemodel_dict['__class__'], basemodel.__class__.__name__)

    def test_save(self):
        """Checks Save"""
        basemodel = BaseModel()
        filestorage1 = FileStorage()
        update = basemodel.__dict__['updated_at']
        basemodel.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertNotEqual(basemodel.__dict__['updated_at'], update)
        update = basemodel.__dict__['updated_at']
        filestorage1.reload()
        self.assertEqual(basemodel.__dict__['updated_at'], update)

    def test_reload(self):
        """Checks Reload"""
        basemodel = BaseModel()
        basemodel.save()
        storage.reload()
        self.assertTrue(os.path.isfile('file.json'))
        key = f"{basemodel.__class__.__name__}.{basemodel.id}"
        self.assertEqual(basemodel.__dict__['updated_at'],
                         storage.all()[key].updated_at)
        basemodel1 = BaseModel()
        basemodel1.save()
        storage.reload()
        self.assertTrue(os.path.isfile('file.json'))
        key1 = f"{basemodel1.__class__.__name__}.{basemodel1.id}"
        self.assertEqual(bm1.__dict__['updated_at'],
                         storage.all()[key1].updated_at)


if __name__ == '__main__':
    unittest.main()
