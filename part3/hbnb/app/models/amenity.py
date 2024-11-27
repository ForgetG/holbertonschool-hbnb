#!/usr/bin/python3
"""Module amenity business logic class
"""
from .base_model import BaseModel
from app.db_app import db


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(255), nullable=False)

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
            if key == 'name':
                if isinstance(value, str) and (len(value) > 50 or len(value) < 1):
                    raise ValueError(f'Name must be less than 50 chars')
