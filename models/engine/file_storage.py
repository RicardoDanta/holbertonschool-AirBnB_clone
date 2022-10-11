#!/usr/bin/python3
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{__class__.__name__}.id"] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            json.dump(f)

    def reload(self):
        with open(self.__file_path, "w") as f:
            json.load(f)
