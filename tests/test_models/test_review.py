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

    def test_instance(self):
        """Checks if an instance of Review is created"""
        review = Review()
        review1 = Review()
        self.assertNotEqual(review.id, review1.id)
        self.assertNotEqual(review.created_at, review1.created_at)
        self.assertNotEqual(review.updated_at, review1.updated_at)
        self.assertIn(review, storage.all().values())
        self.assertIn(review1, storage.all().values())
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_attributes(self):
        """Checks if the attributes are correct"""
        my_review = Review()
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")


if __name__ == '__main__':
    unittest.main()
