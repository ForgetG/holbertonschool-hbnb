#!/usr/bin/python3
"""Module user business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel

class User:
    def __init__(self, first_name, last_name, email, is_admin):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = [] # list to store related places

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp
