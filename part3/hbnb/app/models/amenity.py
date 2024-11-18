#!/usr/bin/python3
"""Module amenity business logic class
"""
from .base_model import BaseModel
from app.db_app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = db.Table('place_amenity',
    db.metadata,
    Column('place_id', Integer, ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', Integer, ForeignKey('amenities.id'), primary_key=True),
    extend_existing=True
)


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
