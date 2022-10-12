#!/usr/bin/python3


"""Console 0.0.1"""


import cmd
import sys
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Print Anything"""
        pass

    def do_help(self, arg):
        """Help"""
        super().do_help(arg)

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
