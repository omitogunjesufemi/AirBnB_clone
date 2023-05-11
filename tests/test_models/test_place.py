"""This module contains the various test for the Place class to assertain
its functionality
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class contains the test suites for the Place class
    """

    def setUp(self):
        """SetUp method to initialize the Place for each instance
        """
        self.place = Place()

    def test_all_place_class_attribute_are_set_to_default(self):
        """Checks if the class attributes are empty string
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
