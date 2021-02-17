#!/usr/bin/python3
"""This module provides 'BaseModel' as base class
from which all other models will be created"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Common definition for all models (attributes/methods)"""

    def __init__(self):
        """Instantiation method which defines attributes"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""

        return "[{model}] ({ident}) {attrs}".format(
            model=self.__class__.__name__,
            ident=self.id,
            attrs=self.__dict__,
            )

    def save(self):
        """This method saves the instance and updates the updated_at time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary containing
        all keys/values of __dict__ of the instance"""

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["created_at"] = self.created_at.isoformat()
        return dictionary
