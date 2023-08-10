#!/usr/bin/python3

import unittest
import json
import datetime
from models.user import User
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand


class TestUser(unittest.TestCase):
    """
    Test suite for the User class
    """

    def test_instance(self):
        """
        Test User instance creation
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """
        Test User attributes
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_to_dict(self):
        """
        Test User to_dict method
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
