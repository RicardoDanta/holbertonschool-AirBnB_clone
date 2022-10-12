#!/usr/bin/python3
"""Classes"""

from models.base_model import BaseModel


class User(BaseModel):
    """Define a Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = "" 
