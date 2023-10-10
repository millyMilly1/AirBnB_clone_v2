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


class FileStorage:
    """
    Class for File Storage
    """
#    __objects = {}
    def __init__(self):
        """Initializer for file_path and object dict"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        #temp_dict = {}
        for key, obj in self.__dict__.items():
            self.__objects[key] = self.__objects.to_dict()

        with open(self.__file_path, 'a+', encoding='utf-8') as file:
            json.dump(self.__objects, file)

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
                    class_name, obj_id = key.split('.')
                    from models.base_model import BaseModel
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
