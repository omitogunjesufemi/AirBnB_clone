"""
This module contains all unittests for all console.py features
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage

class TestHBNBCommandConsole(unittest.TestCase):
    """This contains all tests cases for the Command Console
    """

    def test_help_quit(self):
        """Checks if it prints out the right message for help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            expected_output = " Exits tihe command line interpreter \n"
            self.assertEqual(output, expected_output)

    def test_help_EOF(self):
        """Checks if it prints out the right message for help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()
            expected_output = " Exits the command line interpreter \n"
            self.assertEqual(output, expected_output)

    def test_quit(self):
        """Checks if quit works
        """
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Checks if EOF works
        """
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_empty_line(self):
        """Checks if emptyline works
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue()
            expected_output = ""
            self.assertEqual(output, expected_output)

    def test_create(self):
        """Checks that the  create command works as expected
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertTrue(type(output) is str)
            output = output.replace('-', '').replace('\n', '')
            self.assertTrue(len(output) == 32)
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

    def test_show(self):
        """Checks that the show command works as expected
        """
        inst = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'show User {inst.id}')
            output = f.getvalue()
            expected_output = str(inst) + '\n'
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_destroy(self):
        """Checks that the destroy command works as expected
        """
        inst = City()
        self.assertIn(f'City.{inst.id}', storage.all())

        HBNBCommand().onecmd(f'destroy City {inst.id}')
        self.assertNotIn(f'City.{inst.id}', storage.all())

        # Check that 'destroy' saves to file
        with open(storage._FileStorage__file_path, 'r') as f:
            self.assertNotIn(f'User.{inst.id}', f.read())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_all(self):
        """Checks that the all command works as expected
        """
        inst1 = User()
        inst2 = Place()
        inst3 = Amenity()
        inst4 = State()
        inst5 = Review()
        inst6 = City()
        inst7 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = eval(f.getvalue().replace('\n', ''))

            f.truncate(0)

            HBNBCommand().onecmd('all')
            output2 = eval(f.getvalue().replace('\x00', '').replace('\n', ''))

        self.assertTrue(output != output2)

        outputs = [output, output2]
        for output in outputs:
            self.assertTrue(type(output) is list)
            for str_ in output:
                self.assertTrue(type(str_) is str)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

    def test_update(self):
        """Checks that the update command works as expected
        """
        inst = Place()
        HBNBCommand().onecmd(f'update Place {inst.id} name "Offal"')
        self.assertTrue(inst.name == 'Offal')

        # check that attributes can be updated by passing a dict
        f_cmd = f"Place.update({inst.id}, {{'name': \"Court\"}})"
        cmd_str = HBNBCommand().precmd(f_cmd)
        HBNBCommand().onecmd(cmd_str)
        self.assertEqual(inst.name, 'Court')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue()
            expected_output = "** class name missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NonexistentClass")
            output = f.getvalue()
            expected_output = "** class doesn't exist **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output = f.getvalue()
            expected_output = "** instance id missing **\n"
            self.assertEqual(output, expected_output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 57584939")
            output = f.getvalue()
            expected_output = "** no instance found **\n"
            self.assertEqual(output, expected_output)

    def test_precmd(self):
        """checks that the format of the line set by 'precmd' is as expected
        """
        inst = City()
        ln = HBNBCommand().precmd(f'City.update("{inst.id}", "name", "Offal")')
        self.assertEqual(ln, f'update City "{inst.id}" "name" "Offal"')
