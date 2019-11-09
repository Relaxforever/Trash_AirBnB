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
            my_instance.save()
            print(my_instance.id)
        elif line == None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, clase, arg):
        """Creates a new instance of BaseModel, saves it and print its id"""
        if clase == "BaseModel" and arg != None:
            try:
                all_objs = storage.all()
                for key in all_objs.keys():
                    if (key == arg):
                        break
                print(BaseModel(all_objs[arg]).id)
            except:
                print("** no instance found **")
        elif clase == None:
            print("** class name missing **")
        elif arg == None:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
