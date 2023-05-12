"""This module contains the various test for the User class to assertain
its functionality
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """This class contains the test suites for the User class
    """

    def setUp(self):
        """SetUp method to initialize the User for each instance
        """
        self.user = User()

    def test_email_password_and_names_are_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_create_user_with_kwargs(self):
        """Creates with kwargs
        """
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertTrue(type(new_user.created_at) is datetime)
        self.assertTrue(type(new_user.updated_at) is datetime)
        self.assertTrue(new_user is not self.user)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
