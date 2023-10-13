#!/usr/bin/python3

"""
File Storage: Used for serialization and deserialization to and from
JSON file instead of dictionary.

-   Python doesn’t know how to convert a string to a dictionary (easily)
-   It’s not human readable
-   Using this file with another program in Python
    or other language will be hard.
"""


import json
from os.path import exists
# from models.base_model import BaseModel
# from models.user import User
# from models.city import City
# from models.state import State
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class FileStorage:
    """
    Class for File Storage
    """
    __objects = {}
    __file_path = "file.json"

    def __init__(self):
        """Initializer for file_path and object dict"""
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        temp_dict = {}
        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(temp_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    loaded_data = json.load(file)
                except json.JSONDecodeError:
                    return

            for key, value in loaded_data.items():
                if '.' in key:
                    className, obj_id = key.split('.')
                    from models.base_model import BaseModel
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
