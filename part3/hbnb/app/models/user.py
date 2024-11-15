#!/usr/bin/python3
"""Module user business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    def __init__(self, id, created_at, updated_at, first_name, last_name, email, password):
        from app.services.facade import facade
        super().__init__(id, created_at, updated_at)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_admin = False
        self.places = facade.get_places_by_user_id(id)  # list to store related places

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

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)