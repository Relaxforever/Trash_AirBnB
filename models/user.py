#!/usr/bin/python3
""" User Module that Inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class Used to represent an User
        Attributes
        ----------
        email : str
            email of the user
        password: str
            password of the user
        first_name: str
            first legal name of the user
        last_name: str
            last legal name of the user
    """

    def __init__(self, email=None, password=None, first_name=None,
                 last_name=None):
        """ Parameters
            ----------
        email : str
            email of the user
        password: str
            password of the user
        first_name: str
            first legal name of the user
        last_name: str
            last legal name of the user
        """
        super().__init__()
