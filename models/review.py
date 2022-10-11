#!/usr/bin/python3
"""Class"""

from models.base_models import BaseModel


class Review(BaseModel):
    """Define a Class"""
    place_id = ""
    user_id = ""
    text = ""
