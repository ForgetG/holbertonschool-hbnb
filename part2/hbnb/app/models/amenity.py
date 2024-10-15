#!/usr/bin/python3
"""Module amenity business logic class
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, id, name, created_at, updated_at):
        super().__init__(id, created_at, updated_at)
        self.name = name

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)
