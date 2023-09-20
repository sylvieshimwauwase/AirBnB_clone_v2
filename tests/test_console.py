#!/usr/bin/python3
"""user to test console"""

import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream

class TestCreateCommand(unittest.TestCase):
    """test class to test created parameters and commands"""
    def setUp(self):
        """defining setup"""
        self.console_output = StringIO()
        sys.stdout = self.console_output

    def tearDown(self):
        """ defining class"""
        self.console_output.close()
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        """testing tearDown class"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_with_string_param(self):
        """Testing string parameters"""
        HBNBCommand().onecmd('create User name="John" age=25 score=9.5')
        output = self.console_output.getvalue().strip()
        self.assertTrue(output)
        obj_id = output.split()[0]
        obj = storage.all().get(f'User.{obj_id}')
        self.assertTrue(obj)
        self.assertEqual(obj.name, "John")
        self.assertEqual(obj.age, 25)
        self.assertEqual(obj.score, 9.5)

    def test_create_with_float_param(self):
        """testing float parameters"""
        HBNBCommand().onecmd('create User age=25.5')
        output = self.console_output.getvalue().strip()
        self.assertTrue(output)
        obj_id = output.split()[0]
        obj = storage.all().get(f'User.{obj_id}')
        self.assertTrue(obj)
        self.assertEqual(obj.age, 25.5)

    def test_create_with_integer_param(self):
        """Testing integer parameters"""
        HBNBCommand().onecmd('create User age=25')
        output = self.console_output.getvalue().strip()
        self.assertTrue(output)
        obj_id = output.split()[0]
        obj = storage.all().get(f'User.{obj_id}')
        self.assertTrue(obj)
        self.assertEqual(obj.age, 25)

    def test_create_with_invalid_param(self):
        """Test to show invalid parameters"""
        HBNBCommand().onecmd('create User name=John age=invalid score=9.5')
        output = self.console_output.getvalue().strip()
        self.assertTrue(output)
        self.assertIn("Warning: Invalid parameter format:", output)

if __name__ == '__main__':
    unittest.main()
