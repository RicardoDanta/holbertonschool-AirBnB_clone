#!/usr/bin/python3
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[f"{__class__.__name__}.id"] = obj

    def save(self):
        try:
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(FileStorage.__objects))
        except:
            pass

    def reload(self):
        try:
            with open(FileStorage.__file_path, "w") as f:
                FileStorage.__objects.write(json.loads(f))
        except:
            pass
