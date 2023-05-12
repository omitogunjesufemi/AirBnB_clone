#!/usr/bin/python3
"""This module contains a class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel

    Attributes:
    => email: [string]
    => password: [string]
    => first_name: [string]
    => last_name: [string]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        """This initialises the User class
        """
        super().__init__(**kwargs)
