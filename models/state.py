#!/usr/bin/python3
"""This module contains a class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class State that inherits from BaseModel

    Attributes:
    => name: [string]
    """
    name = ""

    def __init__(self, **kwargs):
        """This initialises the State class
        """
        super().__init__(**kwargs)
