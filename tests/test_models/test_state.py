#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test suite the State class
    """

    def test_inheritance(self):
        """
        Test if State inherits from BaseModel
        """
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of State class
        """
        new_state = State()
        self.assertTrue(hasattr(new_state, 'name'))

    def test_attributes_type(self):
        """
        Test the attributes type of State class
        """
        new_state = State()
        self.assertEqual(type(new_state.name), str)

    def test_save_method(self):
        """
        Test the save method of State class
        """
        new_state = State()
        updated_at = new_state.updated_at
        new_state.save()
        self.assertNotEqual(updated_at, new_state.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of State class
        """
        new_state = State()
        state_dict = new_state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of State class
        """
        new_state = State()
        str_representation = "[State] ({}) {}".format(new_state.id,
                                                      new_state.__dict__)
        self.assertEqual(str(new_state), str_representation)


if __name__ == '__main__':
    unittest.main()
