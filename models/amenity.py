#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the amenity name """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Used to represent an Amenity
        Attributes
        ----------
        name : str
            the name of the amenity
            """

    def __init__(self, name=None, *args, **kwargs):
        """ Parameters
            ----------
            name : str
                the name of the amenity
                """
        super().__init__(*args, **kwargs)
