#!/usr/bin/python3
"""Console 0.0.1"""


import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel

dictionary = {"Amenity": Amenity,
              "BaseModel": BaseModel,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Print Anything"""
        pass

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True

    def do_create(self, arg):
        """Create a new instance"""
        my_args = arg.split()
        if len(my_args[0]) == 0:
            print("** class name missing **")
            return
        try:
            new_ins = eval(my_args[0])()
            new_ins.save()
            print(new_ins.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    print(value)
                    return
            else:
                print("** class doesn't exist **")
                return
        print("** no instance found **")
        
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        my_args = args.split()
        if len(my_args) == 0:
            print("** class name missing **")
            return
        my_dict = storage.all()
        for key, value in my_dict.items():
            if my_args[0] == value.__class__.__name__:
                if len(my_args) == 1:
                    print("** instance id missing **")
                    return
                if my_args[1] == value.id:
                    all_objects = storage.all()
                    all_objects.pop(key)
                    storage.save()
                    return
            else:
                print("** class doesn't exist **")
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
