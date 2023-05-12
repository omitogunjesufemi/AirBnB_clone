"""This module contains the various test for the Place class to assertain
its functionality
"""
import unittest
from models.place import Place
from datetime import datetime


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

    def test_create_place_with_kwargs(self):
        """Creates with kwargs
        """
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertTrue(type(new_place.created_at) is datetime)
        self.assertTrue(type(new_place.updated_at) is datetime)
        self.assertTrue(new_place is not self.place)
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])
