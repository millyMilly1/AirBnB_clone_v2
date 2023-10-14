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

class TestBaseModel_instance(unittest.TestCase):

	def setUp(self):
		""" setup for basemodel """
		self.base_model_instance = BaseModel()
   
	def test_unique_id(self):
		""" Test if each id has a unique ID """
		print("test1")
		instance_1 = BaseModel()
		self.assertEqual(self.base_model_instance.id, instance_1.id)
	
	def test_id_type(self):
		""" test the attribute of id if its type str """ 
		self.assertIsInstance(self.base_model_instance.id, str)


if __name__ == '__main__':
    unittest.main()

