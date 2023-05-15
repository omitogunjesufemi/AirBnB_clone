"""
This module contains all unittests for all console.py features
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommandConsole(unittest.TestCase):
    """This contains all tests cases for the Command Console
    """

    def test_help_quit(self):
        """Checks if it prints out the right message for help quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HNBNBCommand().onecmd("help quit")
            output = f.getvalue()
            expected_output = " Exits tihe command line interpreter"
            self.assertEqual(output, expected_output)
