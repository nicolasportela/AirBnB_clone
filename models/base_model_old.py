#!/usr/bin/python3
"""Provides base class 'BaseModel' from which all other models will be created
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines functionality common to all models (attributes/methods)
	"""

	def __init__(self, *args, **kwargs):
		"""Initialization of an instance
		"""
		if kwargs:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					setattr(self, key, 
					datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
				elif key != "__class__":
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
	
	def __str__(self):
		"""String representation of the BaseModel class
		"""
		return "[{model}] ({ident}) {attrs}".format(
			model=self.__class__.__name__,
			ident=self.id,
			attrs=self.__dict__,
		)

	def save(self):
		"""pdate updated_at with the current datetime
		"""
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		"""Returns a dictionary containing all keys/values of the instance
		"""
		dictionary = self.__dict__.copy()
		dictionary["__class__"] = self.__class__.__name__
		dictionary["updated_at"] = self.updated_at.isoformat()
		dictionary["created_at"] = self.created_at.isoformat()
		return dictionary
