#!/usr/bin/python3
''' This module defines a class, FileStorage,
    that has features which enables it to serialize
    and deserialize objects to and from a file respectively
    '''
import json
import os


class FileStorage():
    ''' This class has private class attrs that
        store the file path and
        a list of objects after deserialisation.
        '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary, _objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w+', encoding='utf-8') as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists)
            if the file doesnt exist, no exception is raised '''
        try:
            json_file = open(self.__file_path, 'r', encoding='utf-8')
        except FileNotFoundError:
            pass
        else:
            dict_from_file = json.load(json_file)
            for key, value in dict_from_file.items():
                class_name = key.split(".")
                from models.base_model import BaseModel
                from models.user import User
                from models.amenity import Amenity
                from models.place import Place
                from models.city import City
                from models.state import State
                from models.review import Review
                self.new(eval(class_name[0] + '(**value)'))
            #self.__object = dict_from_file
            json_file.close()
