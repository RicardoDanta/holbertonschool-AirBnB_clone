#!/usr/bin/python3
"""Test Review"""


import unittest
import models
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """Review"""

    def test_subclass(self):
        """Checks if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Checks if the attributes are correct"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
