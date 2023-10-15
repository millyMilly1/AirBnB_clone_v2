#!/usr/bin/python3

"""
Module for Review class object
Inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class description for Review
    Inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
