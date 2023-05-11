#!/usr/bin/python3
''' This module defines tests for the class, FileStorage '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):
    ''' Test cases for the class, FileStorage '''
    def setUp(self):
        ''' Executes before each test method '''
        self.inst = FileStorage()

    def test_class(self):
        ''' Tests the class features '''
        self.assertTrue(issubclass(FileStorage, object))
        self.assertTrue(isinstance(self.inst, FileStorage))
        self.assertTrue(type(self.inst) is FileStorage)
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)

    def test_all(self):
        ''' Test cases for the method, all '''
        self.assertTrue(type(self.inst.all()) is dict)

    def test_new(self):
        ''' Test cases for the method, new '''
        inst2 = BaseModel()
        self.assertIn(f'{type(inst2).__name__}.{inst2.id}', self.inst.all())
        for value in self.inst.all().values():
            self.assertTrue(type(value).__name__ == 'BaseModel')

    def test_save(self):
        ''' Test cases for the method, save '''
        self.inst.save()
        self.assertTrue(os.path.exists(self.inst._FileStorage__file_path))
        os.remove(self.inst._FileStorage__file_path)

    def test_reload(self):
        ''' Test cases for the method, reload '''
        base_inst = BaseModel()
        base_inst2 = BaseModel()
        self.inst.save()
        base_inst3 = BaseModel()
        self.inst.reload()
        for value in self.inst.all().values():
            self.assertIn(value.id, [base_inst.id, base_inst2.id])
            # Test that only objects from file are created
            self.assertNotEqual(value.id, base_inst3.id)
        os.remove(self.inst._FileStorage__file_path)

        # Test that no exception is raised when the file doesnt exist
        try:
            self.inst.reload()
        except FileNotFoundError:
            self.fail('reload() raised an exception')
