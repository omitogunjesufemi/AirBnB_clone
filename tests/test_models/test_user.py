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
