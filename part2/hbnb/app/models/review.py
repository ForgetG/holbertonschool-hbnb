#!/usr/bin/python3
"""Module review business logic class
"""
from .base_model import BaseModel


class Review(BaseModel):
    def __init__(self, id, text, rating, place_id, user_id):
        super().__init__(id)
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

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
            if key == 'text':
                if  not isinstance(value, str) or len(value) < 1:
                    raise ValueError(f'Text must not be empty')
            elif key == 'rating':
                if isinstance(value, int) and (value > 5 or value < 1):
                    raise ValueError(f'Rating must be between 1 and 5')
            elif key == 'place_id':
                if isinstance(value, str) and len(value) < 1:
                    raise ValueError(f'Place ID must be a non-empty string')
            elif key == 'user_id':
                if isinstance(value, str) and len(value) < 1:
                    raise ValueError(f'User ID must be a non-empty string')
        return data
