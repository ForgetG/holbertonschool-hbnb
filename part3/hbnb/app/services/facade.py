#!/usr/bin/python3
"""Module facade pattern
"""
from app.persistence.repository import SQLAlchemyRepository
import uuid
from ..models.place import Place
from ..models.user import User
from ..models.amenity import Amenity
from ..models.review import Review
from datetime import datetime
from app.services.repositories.user_repository import UserRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = SQLAlchemyRepository(User)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)
        self.amenity_repo = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        # Placeholder method for creating a user
        user = User(**user_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        # User.check(user_data)
        User.validate_request_data(user_data)
        user.hash_password(user.password)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        # Placeholder method for fetching a user by ID
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        # Placeholder method for fetching a user by email
        return self.user_repo.get_by_email(email)

    def get_all_users(self):
        # Placeholder for logic to retrieve a list of all users
        return list(self.user_repo.get_all())

    def update_user(self, user_id, user_data):
        # Placeholder for logic to update a user
        User.validate_request_data(user_data)
        obj = self.get_user(user_id)
        if obj:
            obj.update(user_data)
        return obj

    def delete_user(self, user_id):
        # Placeholder for logic to delete a user
        return self.user_repo.delete(user_id)

    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        amenity = Amenity(**amenity_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        Amenity.validate_request_data(amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        Amenity.validate_request_data(amenity_data)
        obj = self.get_amenity(amenity_id)
        if obj:
            obj.update(amenity_data)
        return obj

    def delete_amenity(self, amenity_id):
        # Placeholder for logic to delete an amenity
        return self.amenity_repo.delete(amenity_id)

    
    # Places methods
    def create_place(self, place_data) -> Place:
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        Place.validate_request_data(place_data)

        if 'owner' in place_data and isinstance(place_data['owner'], dict):
            place_data['owner'] = User(**place_data['owner'])

        place = Place(**place_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        self.place_repo.add(place)
        return place

    def get_place(self, place_id) -> Place:
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list:
        # Placeholder for logic to retrieve all places
        return list(self.place_repo.get_all())

    def get_places_by_user_id(self, user_id) -> list:
        # Placeholder for logic to retrieve all places for a specific user
        return [place for place in self.place_repo.get_all() if place.owner_id == user_id]

    def update_place(self, place_id, place_data) -> Place:
        # Placeholder for logic to update a place
        Place.validate_request_data(place_data)

        obj = self.get_place(place_id)
        if obj:
            obj.update(place_data)
        return obj

    def delete_place(self, place_id) -> bool:
        # Placeholder for logic to delete a place
        return self.place_repo.delete(place_id)

    def create_review(self, review_data):
    # Placeholder for logic to create a review, including validation for user_id, place_id, and rating
        review = Review(**review_data, id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        Review.validate_request_data(review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        # Placeholder for logic to retrieve all reviews
        return list(self.review_repo.get_all())

    def get_reviews_by_place(self, place_id):
        # Placeholder for logic to retrieve all reviews for a specific place
        return [review for review in self.review_repo.get_all() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        # Placeholder for logic to update a review
        Review.validate_request_data(review_data)

        obj = self.get_review(review_id)
        if obj:
            obj.update(review_data)
        return obj


    def delete_review(self, review_id):
        # Placeholder for logic to delete a review
        return self.review_repo.delete(review_id)

facade = HBnBFacade()