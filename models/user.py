#!/usr/bin/python3

"""
Module for User class object
Inherits from BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Class description for User
    Inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
