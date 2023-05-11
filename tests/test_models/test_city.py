"""This module contains the various test for the City class to assertain
its functionality
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """This class contains the test suites for the City class
    """

    def setUp(self):
        """SetUp method to initialize the City for each instance
        """
        self.city = City()

    def test_state_id_and_name_are_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
