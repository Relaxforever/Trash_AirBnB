#!/usr/bin/python3
"""
    Unittester for the AirBnB project
"""
import unittest
import pep8
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """ Tester that checks whetever everything is working as intended """

    def test_pep8_pycodestyle(self):
        """ Tester for pep8/pycodestyle """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors, please fix them")

    def test_instanceof_itself(self):
        """ Tester to see if he is an instance of BaseModel """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_checkif_docstring(self):
        """ Tester to see if the function is correctly documented """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
