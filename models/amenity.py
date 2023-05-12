#!/usr/bin/python3
"""This module contains a class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class Amenity that inherits from BaseModel

    Attributes:
    => name: [string]
    """
    name = ""

    def __init__(self):
        """This initialises the Amenity class
        """
        super().__init__(self)
