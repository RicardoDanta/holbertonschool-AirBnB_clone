#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
class BaseModel:

    def __init__(self, *args, **kwargs):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], format)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], format)
        else:
            storage.new(self)
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__})'
    
    def save(self):
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = f"{self.__class__.__name__}"
        return (new_dict)
