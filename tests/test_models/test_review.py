"""This module contains the various test for the Review class to assertain
its functionality
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """This class contains the test suites for the Review class
    """

    def setUp(self):
        """SetUp method to initialize the Review for each instance
        """
        self.review = Review()

    def test_place_id_user_id_and_text_are_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_create_review_with_kwargs(self):
        """Creates with kwargs
        """
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertTrue(type(new_review.created_at) is datetime)
        self.assertTrue(type(new_review.updated_at) is datetime)
        self.assertTrue(new_review is not self.review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(new_review.user_id, "")
        self.assertEqual(new_review.text, "")
