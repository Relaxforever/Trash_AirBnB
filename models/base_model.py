#!/usr/bin/python3
""" Base Module for the AirBnB Project """


from uuid import uuid4
import datetime


class BaseModel:
    """ Base class that holds """

    def __init__(self):
        """ placeholder """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ placeholder """
        class_nm = self.__class__.__name__
        return "[{}] ({}) {}".format(
            class_nm, self.id,
            self.__dict__)

    def save(self):
        """ placeholder """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ to_dict: this method converts object to a dict
            Return: returns a dictionary containing all keys/values
            of the class
            Args: self. """
        obj = self.__dict__.copy()
        obj["created_at"] = obj["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj["updated_at"] = obj["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj["__class__"] = self.__class__.__name__
        return obj
