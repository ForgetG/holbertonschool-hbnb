#!/usr/bin/python3
"""Module review business logic class
"""
from .base_model import BaseModel


class Review(BaseModel):
    def __init__(self, text, rating):
        super().__init__()
        self.text = text
        self.rating = rating

        self.place = None # store related place
        self.user = None # store related user

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        super().update(data)
