#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test suite for the FileStorage class.
    """

    def test_instance_creation(self):
        """
        Test if an instance of FileStorage can be created.
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_all_method_returns_dict(self):
        """
        Test if the all() method returns a dictionary.
        """
        fs = FileStorage()
        all_objects = fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """
        Test the new() method by adding an object and checking if it exists.
        """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        obj_key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(obj_key, fs.all())

    def test_save_and_reload_methods(self):
        """
        Test saving and reloading objects for data persistence.
        """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        fs2 = FileStorage()
        fs2.reload()
        obj_key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(obj_key, fs2.all())


if __name__ == '__main__':
    unittest.main()
