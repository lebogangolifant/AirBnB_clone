#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath('../..'))
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class."""

    def test_instance_creation(self):
        """Test instance creation and attribute types."""

        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_string_representation(self):
        """Test the string representation of the BaseModel instance."""

        my_model = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(my_model.id,
                                                       my_model.__dict__)
        self.assertIn(expected_string, str(my_model))

    def test_save_method(self):
        """Test the save method's effect on the updated_at attribute."""

        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method's output structure and types."""

        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
