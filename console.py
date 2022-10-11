#!/usr/bin/python3

import cmd
import sys
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def do_create(self, args):
        """Create"""

    def do_help(self, args):
        """Help"""
        return True

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True

    def EmptyLine(self):
        """Print Anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
