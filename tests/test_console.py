"""
This module contains all unittests for all console.py features
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


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

    def test_create_BaseModel(self):
        """Checks if create BaseModel works
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue()
            self.assertTrue(type(output) is str)
            output = output.replace('-', '').replace('\n', '')
            self.assertTrue(len(output) == 32)
