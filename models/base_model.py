#!/usr/bin/python3
""" Base Module for the AirBnB Project """

from uuid import uuid4
from datetime import datetime

class BaseModel:
""" Base class that holds """
    def __init__(self)
        """ placeholder """
        self.id = str(uuid4)
        self.created_at = 
        self.updated_at = self.created_at

    def __str__(self):
        """ placeholder """
        class_nm = self.__class__.__name__
        return "[{}] ({}) <{}>".format(
            class_nm, self.id,
            self.__dict__

    def save(self):
        """ placeholder """

    def to_dict(self):
        """ placeholder """
