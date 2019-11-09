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
        FileStorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj#.to_dict()

    def save(self):
        """ save - serializes __objects to the JSON file
            Args: Void
            Return: Void
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """ reload - deserializes the JSON file to __objects
            Args: Void
            Return: Void
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except:
            pass
