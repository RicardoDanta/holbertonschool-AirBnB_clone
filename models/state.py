#!/usr/bin/python3
"""Classes"""

from models.base_models import BaseModel


class State(BaseModel):
    """Define a Class"""
    def __init__(self, name):
        """Name"""
        self.name = ""
