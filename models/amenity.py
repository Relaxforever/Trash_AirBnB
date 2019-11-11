#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the amenity name """
fromd models import BaseModel


class Amenity(BaseModel):
    """ Class Used to represent an Amenity
        Attributes
        ----------
        name : str
            the name of the amenity
            """

    def __init__(self, name=None):
        """ Parameters
            ----------
            name : str
                the name of the amenity
                """
        super().__init__()
