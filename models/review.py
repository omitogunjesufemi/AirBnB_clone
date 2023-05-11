#!/usr/bin/python3
"""This module contains a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class Review that inherits from BaseModel

    Attributes:
    => place_id: [string] (default = empty) :- This will be the Place.id
    => user_id: [string] (default = empty) :- This will be the User.id
    => text: [string] (default = empty)
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """This initialises the Review class
        """
        super().__init__(self)
