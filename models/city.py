#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the city name """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class Used to represent an American City
        Attributes
        ----------
        state_id: str
            it will be the id of the state
        name : str
            the name of the city
            """

    def __init__(self, state_id=None, name=None):
        """ Parameters
            ----------
            state_id : str
                The id of the state
            name : str
                the name of the state
                """
        super().__init__()
