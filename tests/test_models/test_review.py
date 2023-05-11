"""This module contains the various test for the Review class to assertain
its functionality
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """This class contains the test suites for the Review class
    """

    def setUp(self):
        """SetUp method to initialize the Review for each instance
        """
        self.review = Review()

    def test_state_id_and_name_are_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
