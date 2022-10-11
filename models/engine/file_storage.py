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
        try:
            with open(self.__file_path, "w") as f:
                f.write(json.dumps(self.__objects))
        except:
            pass

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f)
        except:
            pass
