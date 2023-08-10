#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test the Place class
    """

    def test_inheritance(self):
        """
        Test if Place inherits from BaseModel
        """
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of Place class
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, 'city_id'))
        self.assertTrue(hasattr(new_place, 'user_id'))
        self.assertTrue(hasattr(new_place, 'name'))
        self.assertTrue(hasattr(new_place, 'description'))
        self.assertTrue(hasattr(new_place, 'number_rooms'))
        self.assertTrue(hasattr(new_place, 'number_bathrooms'))
        self.assertTrue(hasattr(new_place, 'max_guest'))
        self.assertTrue(hasattr(new_place, 'price_by_night'))
        self.assertTrue(hasattr(new_place, 'latitude'))
        self.assertTrue(hasattr(new_place, 'longitude'))
        self.assertTrue(hasattr(new_place, 'amenity_ids'))

    def test_attributes_type(self):
        """
        Test the attributes type of Place class
        """
        new_place = Place()
        self.assertEqual(type(new_place.city_id), str)
        self.assertEqual(type(new_place.user_id), str)
        self.assertEqual(type(new_place.name), str)
        self.assertEqual(type(new_place.description), str)
        self.assertEqual(type(new_place.number_rooms), int)
        self.assertEqual(type(new_place.number_bathrooms), int)
        self.assertEqual(type(new_place.max_guest), int)
        self.assertEqual(type(new_place.price_by_night), int)
        self.assertEqual(type(new_place.latitude), float)
        self.assertEqual(type(new_place.longitude), float)
        self.assertEqual(type(new_place.amenity_ids), list)

    def test_save_method(self):
        """
        Test the save method of Place class
        """
        new_place = Place()
        updated_at = new_place.updated_at
        new_place.save()
        self.assertNotEqual(updated_at, new_place.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Place class
        """
        new_place = Place()
        place_dict = new_place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of Place class
        """
        new_place = Place()
        str_representation = "[Place] ({}) {}".format(new_place.id,
                                                      new_place.__dict__)
        self.assertEqual(str(new_place), str_representation)


if __name__ == '__main__':
    unittest.main()
