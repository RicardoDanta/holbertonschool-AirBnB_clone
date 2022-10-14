#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This function is the constructor for the BaseModel
        class. It creates a new instance of the
        BaseModel class and assigns it an id, created_at, and updated_at
        """
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
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """
        The function returns a string representation of the object
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        The save function updates the updated_at
        attribute of the object to the current time and saves
        the object to the JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This function takes in an object and
        returns a dictionary representation of the object
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat("T")
        new_dict["updated_at"] = self.updated_at.isoformat("T")
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
