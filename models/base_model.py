#!/usr/bin/python3
"""This module contains the BaseModel class which defines all common attributes
or methods of other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This class defines all common attributes/methods for other classes

    Attributes:
    >> id: [string] - assign with an uuid when an instance is created using
           using uuid.uuid4() to have a unique id for each BaseModel
    >> created_at: [datetime] - assign with the current datetime when an
                   instance is created
    >> updated_at: [datetime] - assign with the current datetime when an
                   instance is created, and it will be updated everytime the
                   object is changed

    Methods:
    >> save(self): updates the public instance attribute update_at with the
    current datetime
    >> to_dict(self): returns a dictionary containing all keys/values of
    __dict__ of the instance
    """

    def __init__(self, *args, **kwargs):
        """This initialises the BaseModel class
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    @staticmethod
    def get_custom_attrs(inst):
        ''' Returns a dict containing the only the custom class attrs.
            The dictionary is created from the return value
            of 'vars(inst.__class__.__name__) '''
        from models.user import User
        vars_call = 'vars(' + inst.__class__.__name__ + ')'
        attrs = eval(vars_call)
        custom_attrs = {}
        for key in attrs:
            if not key.startswith('__'):
                custom_attrs[key] = attrs[key]

        return (custom_attrs)

    def __str__(self):
        """String representation of the BaseModel Class
        """
        if self.__class__.__name__ != 'BaseModel':
            custom_attrs = BaseModel.get_custom_attrs(self)
            custom_attrs.update(self.__dict__.copy())
            str_ = f'[{self.__class__.__name__}] ({self.id}) {custom_attrs}'
        else:
            str_ = f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

        return (str_)

    def save(self):
        """Public instance method that updates the public instance attribute
        update_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Public instance method that returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['updated_at'] = self.updated_at.isoformat()
        new_dictionary['created_at'] = self.created_at.isoformat()

        if self.__class__.__name__ != 'BaseModel':
            new_dictionary.update(BaseModel.get_custom_attrs(self))
        return (new_dictionary)
