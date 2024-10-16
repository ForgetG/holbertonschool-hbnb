#!/usr/bin/python3
"""Module facade pattern
"""
from app.persistence.repository import InMemoryRepository
from ..models.place import Place


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        # Placeholder method for creating a user
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        # Placeholder method for fetching a user by ID
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        # Placeholder method for fetching a user by email
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return list(self.amenity_repo.values())

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        obj = self.get(amenity_id)
        if obj:
            obj.update(amenity_data)
    
    # Places methods
    def create_place(self, place_data) -> Place:
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        Place.validate_request_data(place_data)

        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id) -> Place:
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list:
        # Placeholder for logic to retrieve all places
        return list(self.place_repo.values())

    def update_place(self, place_id, place_data) -> Place:
        # Placeholder for logic to update a place
        Place.validate_request_data(place_data)

        obj = self.get_place(place_id)
        if obj:
            obj.update(place_data)
        return obj
