#!/usr/bin/python3
"""Module user business logic class
"""
from app.bcrypt_app import bcrypt
from app.db_app import db
import uuid
from .base_model import BaseModel
import re

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

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