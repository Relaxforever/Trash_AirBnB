#!/usr/bin/python3
""" User Module Inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Base Class that holds all user information """

    def __init__(self, email=None, password=None, first_name=None,
                 last_name=None):
        """ Initiziaializer file """
        super().__init__()
