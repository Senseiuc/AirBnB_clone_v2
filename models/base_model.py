#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
<<<<<<< HEAD
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from os import getenv

time_fmt = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models
>>>>>>> 2d124c8e0c972c0e429279c1410b7a68c4c5ffcd


Base = declarative_base()

class BaseModel:
<<<<<<< HEAD
    """The BaseModel class from which future classes will be derived"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, time_fmt)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, time_fmt)
=======
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value)
>>>>>>> 2d124c8e0c972c0e429279c1410b7a68c4c5ffcd

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """returns a dictionary containing all keys/values of the instance"""
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
        if not save_to_disk:
            new_dict.pop('password', None)
        return new_dict

    def delete(self):
        """Delete current instance from storage by calling its delete method"""
=======
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """
        to delete the current instance from the storage
        """
>>>>>>> 2d124c8e0c972c0e429279c1410b7a68c4c5ffcd
        models.storage.delete(self)
