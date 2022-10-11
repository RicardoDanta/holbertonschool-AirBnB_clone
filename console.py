#!/usr/bin/python3

import cmd
import sys
from models import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB"""
    prompt = "(hbnb)"

    def EmptyLine(self):
        """Print Anything"""
        pass

    def do_help(self, args):
        """Help"""
        return True

    def do_EOF(self, args):
        """End of File"""
        return True

    def do_quit(self, args):
        """Quit"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
