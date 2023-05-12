"""This module contains the various test for the Amenity class to assertain
its functionality
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """This class contains the test suites for the Amenity class
    """

    def setUp(self):
        """SetUp method to initialize the Amenity for each instance
        """
        self.amenity = Amenity()

    def test_amenity_names_are_empty_string(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.amenity.name, "")

    def test_create_amenity_with_kwargs(self):
        """Creates with kwargs
        """
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertTrue(type(new_amenity.created_at) is datetime)
        self.assertTrue(type(new_amenity.updated_at) is datetime)
        self.assertTrue(new_amenity is not self.amenity)
        self.assertEqual(new_amenity.name, "")
