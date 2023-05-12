"""This module contains the various test for the State class to assertain
its functionality
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """This class contains the test suites for the State class
    """

    def setUp(self):
        """SetUp method to initialize the State for each instance
        """
        self.state = State()

    def test_state_name_is_an_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.state.name, "")

    def test_create_state_with_kwargs(self):
        """Creates with kwargs
        """
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertTrue(type(new_state.created_at) is datetime)
        self.assertTrue(type(new_state.updated_at) is datetime)
        self.assertTrue(new_state is not self.state)
        self.assertEqual(new_state.name, "")
