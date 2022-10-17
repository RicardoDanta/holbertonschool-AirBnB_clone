#!/usr/bin/python3
""" tests for the console """

import unittest
import os
import os.path import exists
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class Test_console(unittest.TestCase):
    """Testing the Console"""

    def test_prompt(self):
        """Check the Prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_EOF(self):
        """Check End Of File"""
        self.assertEqual(True, HBNBCommand().do_EOF(None))

    def test_quit(self):
        """Check Quit """
        with self.assertRaises(SystemExit):
            HBNBCommand().do_quit(None)

    def test_create(self):
        """Checking Create """
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel.json"))
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel2.json"))
        HBNBCommand().do_create("BaseModel")
        self.assertTrue(exists("BaseModel3.json"))

    def test_all(self):
        """Check All"""
        HBNBCommand().do_create("BaseModel")
        HBNBCommand().do_create("BaseModel")
        HBNBCommand().do_all("BaseModel")
        self.assertTrue(exists("BaseModel.json"))
        self.assertTrue(exists("BaseModel2.json"))
