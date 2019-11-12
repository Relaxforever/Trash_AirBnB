#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the state name """
fromd models.base_model import BaseModel


class State(BaseModel):
    """ Class Used to represent an American State
        Attributes
        ----------
        name : str
            the name of the state
            """

    def __init__(self, name=None):
        """ Parameters
            ----------
            name : str
                the name of the state
                """
        super().__init__()
