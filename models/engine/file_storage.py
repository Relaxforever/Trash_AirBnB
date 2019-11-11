#!/usr/bin/python3
""" File storage Module """
import json


class FileStorage:
    """ Saves the instances in a json file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all - Return the dictionary of objects
            Args: Void
            Return: The dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """ new - Set the object with key <obj class name>.id
            Args: obj
            Return: Void
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ save - serializes __objects to the JSON file
            Args: Void
            Return: Void
        """
        tmp = {}
        for key, value in FileStorage.__objects.items():
            tmp[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(tmp, f)

    def reload(self):
        """ reload - deserializes the JSON file to __objects
            Args: Void
            Return: Void
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp = json.load(f)
                for key, value in tmp.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass
