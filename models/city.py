#!/usr/bin/python3

"""
Module for City class object
Inherits from BaseModel
"""


from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """
    Class description for City
    Inherits from BaseModel
    """
    name = ""
    state_id = ""
