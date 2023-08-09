#!/usr/bin/python3
"""FileStorage module to store objects"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class responsible for managing the
    serialization and deserialization of instances to and from
    JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns:
            dict: A dictionary of all stored instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new instance to the storage.

        Args:
            obj (BaseModel): The instance to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes instances to the JSON file.
        """
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes instances from the JSON file.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
