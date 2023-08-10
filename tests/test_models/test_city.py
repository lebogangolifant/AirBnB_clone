#!/usr/bin/python3

import unittest
import json
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Test suite for the City class
    """

    def test_inheritance(self):
        """
        Test if City inherits from BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of City class
        """
        new_city = City()
        self.assertTrue(hasattr(new_city, 'state_id'))
        self.assertTrue(hasattr(new_city, 'name'))

    def test_attributes_type(self):
        """
        Test the attributes type of City class
        """
        new_city = City()
        self.assertEqual(type(new_city.state_id), str)
        self.assertEqual(type(new_city.name), str)

    def test_save_method(self):
        """
        Test the save method of City class
        """
        new_city = City()
        updated_at = new_city.updated_at
        new_city.save()
        self.assertNotEqual(updated_at, new_city.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of City class
        """
        new_city = City()
        city_dict = new_city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of City class
        """
        new_city = City()
        str_representation = "[City] ({}) {}".format(new_city.id,
                                                     new_city.__dict__)
        self.assertEqual(str(new_city), str_representation)


if __name__ == '__main__':
    unittest.main()
