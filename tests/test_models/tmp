#!/usr/bin/python3
"""Tests the base model module"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test base_model class"""

    def test_init(self):
        """test init module"""
        my_model = BaseModel()
        my_model.name = "Mine"

    def test_save(self):
        """Test save method"""
        my_model = BaseModel()
        my_model.name = "Hello"
        my_model.save()
        model_dict = {}
        model_dict['id'] = my_model.id
        model_dict['created_at'] = my_model.created_at
        model_dict['updated_at'] = my_model.updated_at
        model_dict['name'] = "Hello"
        string = f'[BaseModel] ({my_model.id}) {model_dict}'
        self.assertEqual(str(my_model), string)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()
        my_model.name = "Hello"
        my_model.save()
        model_dict = {}
        model_dict['id'] = my_model.id
        model_dict['created_at'] = my_model.created_at.isoformat(
                timespec='microseconds')
        model_dict['updated_at'] = my_model.updated_at.isoformat(
                timespec='microseconds')
        model_dict['name'] = "Hello"
        model_dict['__class__'] = 'BaseModel'
        self.assertEqual(my_model.to_dict(), model_dict)

    def test_str(self):
        """Test str method"""
        my_model = BaseModel()
        model_dict = {}
        model_dict['id'] = my_model.id
        model_dict['created_at'] = my_model.created_at
        model_dict['updated_at'] = my_model.updated_at
        string = f'[BaseModel] ({my_model.id}) {model_dict}'
        self.assertEqual(str(my_model), string)


if __name__ == '__main__':
    unittest.main()
