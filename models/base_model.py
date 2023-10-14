#!/usr/bin/python4

"""
BaseModel for AirBnB Clone - Console

"""


from datetime import datetime
from models import storage
import json
import uuid
# import models


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
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of the class"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
                )

    def save(self):
        """Sets an updated time for every changes made"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts class object to dict"""
        result_dict = {}
        for key, val in self.__dict__.items():
            result_dict[key] = val
        result_dict['__class__'] = type(self).__name__
        result_dict['created_at'] = result_dict['created_at'].isoformat()
        result_dict['updated_at'] = result_dict['updated_at'].isoformat()
        return result_dict

    def to_json(self):
        """Converts dict to JSON"""
        return json.dumps(self.to_dict())
