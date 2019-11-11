#!/usr/bin/python3
""" Console module """
import cmd
from models.base_model import BaseModel
from models import storage


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
                    #for key in all_objs.keys():
                    #    if (key == arg):
                    #        break
                    print(all_objs["BaseModel." + splitted[1]])
                except:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(splitted) == 1:
            print("** instance id missing **")
        elif len(splitted) == 0:
            print("** class name missing **")

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
