#!/usr/bin/python3
"""This module contains a class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherits from BaseModel

    Attributes:
    => state_id: [string] :- This will be the state.id
    => name: [string]
    """
    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """This initialises the City class
        """
        super().__init__(**kwargs)
