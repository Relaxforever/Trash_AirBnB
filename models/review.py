#!/usr/bin/python3
""" Subclass of BaseModel in charge of saving the review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Used to write a review and leave the user_id and place_id
        Attributes
        ----------
        place_id: str
            it will be the id of the place
        user_id : str
            the id of the user
        text: str
            the text/review
            """

    def __init__(self, place_id="", user_id="", text="", *args, **kwargs):
        """ Parameters
            ----------
            place_id : str
                The id of the place
            user_id : str
                the user id
            text_id: str
                the user text/review
                """
        super().__init__(*args, **kwargs)
