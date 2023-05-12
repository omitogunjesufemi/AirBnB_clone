"""This module contains the various test for the City class to assertain
its functionality
"""
import unittest
from models.city import City
from datetime import datetime


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

    def test_create_city_with_kwargs(self):
        """Creates with kwargs
        """
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertTrue(type(new_city.created_at) is datetime)
        self.assertTrue(type(new_city.updated_at) is datetime)
        self.assertTrue(new_city is not self.city)
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
