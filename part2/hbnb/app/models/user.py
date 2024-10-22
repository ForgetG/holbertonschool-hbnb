#!/usr/bin/python3
"""Module user business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
import re

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    def __init__(self, id, first_name, last_name, email):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.places = []  # list to store related places

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)

    @staticmethod
    def validate_request_data(data: dict):
        for key in data.keys():
            value = data[key]
            if key == 'first_name' or key == 'last_name':
                if isinstance(value, str) and (len(value) > 50 or len(value) < 1):
                    raise ValueError(f"String must be less than 50 chars or not empty")
            elif key == 'email':
                if (re.match(regex, data["email"])):
                    return data
                else:
                    raise ValueError(f"Email must follow standard email format")
            elif key == 'id':
                try:
                    uuid_user = uuid.UUID(data[key], version=4)
                except ValueError:
                    return ValueError
                return data
