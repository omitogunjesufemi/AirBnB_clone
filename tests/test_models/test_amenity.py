"""This module contains the various test for the Amenity class to assertain
its functionality
"""
import unittest
from models.amenity import Amenity


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
