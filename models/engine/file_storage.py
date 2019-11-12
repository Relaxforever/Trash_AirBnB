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
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(FileStorage.__file_path, "r") as f:
                tmp = json.load(f)
                for key, value in tmp.items():
                    #FileStorage.__objects[key] = globals()[str(value["__class__"])](**value)
                    if value["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value["__class__"] == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif value["__class__"] == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif value["__class__"] == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif value["__class__"] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value["__class__"] == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif value["__class__"] == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except:
            pass
