#!/usr/bin/python3
"""Module reviews API endpoint
"""
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'You cannot review your own place.')
    @api.response(400, 'You have already reviewed this place.')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        current_user = get_jwt_identity()
        review_data = api.payload
        review_data["user_id"] = current_user["id"]

        if review_data['user_id'] != current_user["id"]:
            return {'error': 'Unauthorized action'}, 403

        user_places = facade.get_places_by_user_id(review_data["user_id"])
        for place in user_places:
            if review_data["place_id"] == place.id:
                return {'error': 'You cannot review your own place.'}, 400 

        place_reviews = facade.get_reviews_by_place(review_data["place_id"])
        for review in place_reviews:
            if review_data["user_id"] == review.user_id:
                return {'error': 'You have already reviewed this place.'}, 400


        try:
            new_review = facade.create_review(review_data)
        except ValueError as error:
            return {'error': "Invalid input data"}, 400

        return {
            'id': new_review.id,
            'text': new_review.text,
            'rating': new_review.rating,
            'user_id': new_review.user_id,
            'place_id': new_review.place_id
        }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        list_of_reviews = facade.get_all_reviews()
        return [{'id': review.id, 'text': review.text, 'rating': review.rating} for review in list_of_reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {'id': review_id, 'text': review.text, 'rating': review.rating, 'user_id': review.user_id, 'place_id': review.place_id}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        current_user = get_jwt_identity()
        review_data = api.payload
        review_data["user_id"] = current_user["id"]

        if review_data['user_id'] != current_user["id"]:
            return {'error': 'Unauthorized action'}, 403

        try:
            updated_review = facade.update_review(review_id, review_data)
        except ValueError as error:
            return {'error': 'Invalid input data'}, 400

        if not updated_review:
            return {'error': 'Review not found'}, 404
        return {"message": "Review updated successfully"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to delete a review
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)

        if review["user_id"] != current_user["id"]:
            return {'error': 'Unauthorized action'}, 403

        if not review:
            return {'error': 'Review not found'}, 404
        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        # Placeholder for logic to return a list of reviews for a place
        list_of_reviews = facade.get_reviews_by_place(place_id)
        return [{'id': review.id, 'text': review.text, 'rating': review.rating} for review in list_of_reviews], 200
