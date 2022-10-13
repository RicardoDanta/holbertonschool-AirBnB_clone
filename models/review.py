#!/usr/bin/python3
"""Create a class Review that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Define a Class"""
    place_id = ""
    user_id = ""
    text = ""
