#!/usr/bin/python3
''' This module defines a class, FileStorage,
    that has features which enables it to serialize
    and deserialize objects to and from a file respectively
    '''
import json


class FileStorage():
    ''' This class has private class attrs that
        store the file path and
        a list of objects after deserialisation.
        '''
    _file_path = 'file.json'
    _objects = {}

    def all(self):
        ''' Returns the dictionary, _objects '''
        return self._objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self._objects[key] = obj.to_dict()

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        with open(self._file_path, 'w', encoding='utf-8') as json_file:
            str = json.dumps(self._objects)
            print(str)

    def reload(self):
        ''' deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
            if the file doesnt exist, no exception is raised '''
        try:
            json_file = open(self._file_path, 'r', encoding='utf-8')
        except:
            pass
        else:
            self._objects = json.load(json_file)
            json_file.close()
