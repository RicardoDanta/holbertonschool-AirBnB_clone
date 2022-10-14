#!/usr/bin/python3
"""Unittests for BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel"""

    def test_save(self):
        basemodel = BaseModel()
        basemodel.save()
        self.assertNotEqual(basemodel.created_at, basemodel.updated_at)

    def test_to_dict(self):
        basemodel = BaseModel()
        basemodel.to_dict()
        self.assertNotEqual(basemodel.created_at, basemodel.update_at, self.__class__)


if __name__ == '__main__':
    unittest.main()
