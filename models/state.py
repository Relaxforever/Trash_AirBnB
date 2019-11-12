#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the state name """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class Used to represent an American State
        Attributes
        ----------
        name : str
            the name of the state
            """

    def __init__(self, name=None, *args, **kwargs):
        """ Parameters
            ----------
            name : str
                the name of the state
                """
        super().__init__(*args, **kwargs)
