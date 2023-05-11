#!/usr/bin/python3
"""This module contains a class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class Place that inherits from BaseModel

    Attributes:
    => city_id: [string] (default = empty) :- It will be the City.id
    => user_id: [string] (default = empty) :- It will be the User.id
    => name: [string] (default = empty)
    => description: [string] (default = empty)
    => number_rooms: [integer] (default = 0)
    => number_bathrooms: [integer] (default = 0)
    => max_guest: [integer] (default = 0)
    => price_by_night: [integer] (default = 0)
    => latitude: [float] (default = 0.0)
    => longitude: [float] (default = 0.0)
    => amenity_ids: [list of string] (default = empty list)
                    It will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        """This initialises the Place class
        """
        super().__init__(self)
