#!/usr/bin/python3
""" test model for base_model.py
BaseModel cases:
        test_id_generation
        test_deserialization
"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests BaseModel class """
    def test_init(self):
        """ setup for basemodel """
        instance1 = BaseModel()
        instance2 = BaseModel()

    def test_unique_id(self):
        # Create two instances of BaseModel
        instance1 = BaseModel()
        instance2 = BaseModel()

        # Assert that the IDs of the two instances are different
        self.assertNotEqual(instance1.id, instance2.id)

    def test_id_type(self):
        """ test the attribute of id if its type str """
        instance1 = BaseModel()
        self.assertIsInstance(instance1.id, str)

    def test_id_format(self):
        """ tests if id attribute matches format uuid """
        instance1 = BaseModel()
        id_format = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]'
        '{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        self.assertTrue(id_format, instance1.id)


if __name__ == '__main__':
    unittest.main()
