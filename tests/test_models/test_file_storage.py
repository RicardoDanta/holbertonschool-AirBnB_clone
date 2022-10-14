#!/usr/bin/python3
"""Test FileStorage"""

import unittest
from models.engine import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing"""

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.self.__objects)

    def test_new(self):
        storage = FileStorage()
        self.assertEqual(storage.self.__objects)


if __name__ == '__main__':
    unittest.main()
