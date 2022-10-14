#!/usr/bin/python3
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        It returns all the objects in the class
        """
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Takes in an instance of FileStorage and writes the JSON string
        representation of the dictionary __objects to the file __file_path
        """
        new_dict = {}
        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        It opens the file, reads it, and then
        converts the JSON string into a Python object
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                aux = json.loads(f.read())
                for key, val in aux.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
