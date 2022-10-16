#!/usr/bin/python3
"""
    module
"""
import models
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class Test_Basemodel():
    """tests to base model"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def instance_exist(self):
        self.assertIn(BaseModel, models.storage.all().values())

    def id(self):
        self.assertEqual(str, type(BaseModel().id))

    def created_at(self):
        self.assertEqual(datatime, type(BaseModel().created_at))

    def updated_at(self):
        self.assertEqual(datatime, type(BaseModel().updated_at))

    def __str__(self):
        """test str"""
        basemodel = BaseModel()
        self.assertEqual(f"[{type(basemodel).__name__}] ({basemodel.id}) {basemodel.__dict__}", str(m))

    def args_unused(self):
        basemodel = BaseModel()
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_save(self):
        basemodel = BaseModel()
        basemodel.save()
        bmid = "BaseModel." + basemodel.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


    def test_with_args(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)

    def test_output(self):
        date = datatime.today()
        basemodel = BaseModel()
        basemodel.id = "123456"
        basemodel.created_at = updated_at = date
        tdict = {'id': '123456', '__class__': 'BaseModel',
                 'created_at': date.isoformat(), 'updated_at': date.isoformat()}

    def equal_or_not(self):
        """equals"""
        id_to_compare = BaseModel()
        id_compare = BaseModel()
        self.assertNotEqual(id_compare, id_to_compare)

    def test_datetime_attr_are_str(self):
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(str, type(basemodel_dict["created_at"]))
        self.assertEqual(str, type(basemodel_dict["updated_at"]))

    def tests_to_dict(self):
        """test dict"""
        basemodel = BaseModel()
        self.assertEqual(basemodel.to_dict()["id"], bm.id)
        self.assertEqual(basemodel.to_dict()["created_at"], basemodel.created_at.isoformat())
        self.assertEqual(basemodel.to_dict()["updated_at"], basemodel.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
