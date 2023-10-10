#!/usr/bin/python3

"""
BaseModel for AirBnB Clone - Console

"""


from .__init__ import storage
from datetime import datetime
import json
import uuid


class BaseModel:
    """
    The BaseModel
    All other models inherits from this.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization for all models based on BaseModel
        Initializes id, craeted_at and updated_at
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Strimg representation of the class
        """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """
        Sets an updated time for every changes made
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts class onject to dict
        """
        self.created_at = datetime.isoformat(self.created_at)
        self.updated_at = datetime.isoformat(self.updated_at)
        result_dict = self.__dict__
        result_dict['__class__'] = type(self).__name__
        return result_dict

    def to_json(self):
        """
        Converts dict to JSON
        """
        return json.dumps(self.to_dict())
