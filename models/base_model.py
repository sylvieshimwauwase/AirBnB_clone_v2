#!/usr/bin/python3
"""Defines the BaseModel class."""

from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, time)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, time)

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        if '_password' in new_dict:
            new_dict['password'] = new_dict['_password']
            new_dict.pop('_password', None)
        if 'amenities' in new_dict:
            new_dict.pop('amenities', None)
        if 'reviews' in new_dict:
            new_dict.pop('reviews', None)
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop('_sa_instance_state', None)
        """if not save_to_disk:
            new_dict.pop('password', None)"""
        return new_dict

    def delete(self):
        """ delete object
        """
        models.storage.delete(self)
