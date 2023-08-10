#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test suite for the Review class
    """

    def test_inheritance(self):
        """
        Test if Review inherits from BaseModel
        """
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_attributes(self):
        """
        Test the attributes of Review class
        """
        new_review = Review()
        self.assertTrue(hasattr(new_review, 'place_id'))
        self.assertTrue(hasattr(new_review, 'user_id'))
        self.assertTrue(hasattr(new_review, 'text'))

    def test_attributes_type(self):
        """
        Test the attributes type of Review class
        """
        new_review = Review()
        self.assertEqual(type(new_review.place_id), str)
        self.assertEqual(type(new_review.user_id), str)
        self.assertEqual(type(new_review.text), str)

    def test_save_method(self):
        """
        Test the save method of Review class
        """
        new_review = Review()
        updated_at = new_review.updated_at
        new_review.save()
        self.assertNotEqual(updated_at, new_review.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of Review class
        """
        new_review = Review()
        review_dict = new_review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_str_method(self):
        """
        Test the __str__ method of Review class
        """
        new_review = Review()
        str_representation = "[Review] ({}) {}".format(new_review.id,
                                                       new_review.__dict__)
        self.assertEqual(str(new_review), str_representation)


if __name__ == '__main__':
    unittest.main()
