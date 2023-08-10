#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class
    """

    def test_inheritance(self):
        """
        Test if Amenity inherits from BaseModel
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of Amenity class
        """
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, 'name'))

    def test_attributes_type(self):
        """
        Test the attributes type of Amenity class
        """
        new_amenity = Amenity()
        self.assertEqual(type(new_amenity.name), str)

    def test_save_method(self):
        """
        Test the save method of Amenity class
        """
        new_amenity = Amenity()
        updated_at = new_amenity.updated_at
        new_amenity.save()
        self.assertNotEqual(updated_at, new_amenity.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Amenity class
        """
        new_amenity = Amenity()
        amenity_dict = new_amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of Amenity class
        """
        new_amenity = Amenity()
        str_representation = "[Amenity] ({}) {}".format(new_amenity.id,
                                                        new_amenity.__dict__)
        self.assertEqual(str(new_amenity), str_representation)


if __name__ == '__main__':
    unittest.main()
