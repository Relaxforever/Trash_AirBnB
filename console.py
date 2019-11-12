#!/usr/bin/python3
""" Console module """
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ HBNB console """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit from the console prompt"""
        return True

    def do_EOF(self, line):
        """EOF quit from the console prompt"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and print its id"""
        if line == "BaseModel":
            my_instance = BaseModel()
            print(my_instance.id)
            my_instance.save()
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Creates a new instance of BaseModel, saves it and print its id"""
        splitted = line.split()
        if len(splitted) == 2:
            if splitted[0] == "BaseModel":
                try:
                    all_objs = storage.all()
                    print(all_objs["BaseModel." + splitted[1]])
                except:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(splitted) == 0:
            print("** class name missing **")
        elif len(splitted) == 1:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name."""
        if line == "BaseModel":
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if obj.__class__.__name__ == "BaseModel":
                    print(obj)
        elif len(line) == 0:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        splitted = line.split()
        if len(splitted) == 2:
            if splitted[0] == "BaseModel":
                try:
                    all_objs = storage.all()
                    del all_objs["BaseModel." + splitted[1]]
                    storage.save()
                except:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(splitted) == 0:
            print("** class name missing **")
        elif len(splitted) == 1:
            print("** instance id missing **")

    def do_update(self, line):
        """Updates an instance based on the class name
            and id by adding or updating attribute"""

        splitted = line.split()
        all_objs = storage.all()
        if len(splitted) == 0:
            print("** class name missing **")
        elif splitted[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(splitted) == 1:
            print("** instance id missing **")
        elif "BaseModel." + splitted[1] not in all_objs.keys():
            print("** no instance found **")
        elif len(splitted) == 2:
            print("** attribute name missing **")
        elif len(splitted) == 3:
            print("** value missing **")
        else:
            if "BaseModel." + splitted[1] in all_objs.keys():
                setattr(all_objs["BaseModel." + splitted[1]],
                        splitted[2], splitted[3])
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
