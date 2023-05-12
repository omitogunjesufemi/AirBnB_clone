"""This module contains the various test for the State class to assertain
its functionality
"""
import unittest
from models.state import State


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
