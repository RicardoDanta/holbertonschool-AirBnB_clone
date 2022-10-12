#!/usr/bin/python3
import os
from socket import AF_IPX
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.user import User
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review
from models.base_model import BaseModel
import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                aux = json.loads(f.read())
                for key, val in aux.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
