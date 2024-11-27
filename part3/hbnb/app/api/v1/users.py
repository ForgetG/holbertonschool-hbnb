#!/usr/bin/python3
"""Module users API endpoint
"""
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
import json


api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/me')
class MeResource(Resource):
    @jwt_required()
    def get(self):
        current_user = json.loads(get_jwt_identity())
        user = facade.get_user(current_user['id'])
        if not user:
           return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'places': [place.id for place in user.places]
        }, 200


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    # @jwt_required()
    def post(self):
        """Register a new user"""
        current_user = json.loads(get_jwt_identity())
        user_data = api.payload

        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')
        is_admin = user_data.get('is_admin', True)

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        user_data['is_admin'] = is_admin

        try:
           new_user = facade.create_user(user_data)
        except ValueError as error:
           return {'error': 'Invalid input data'}, 400
        return {'id': new_user.id, 'message': 'User successfully created'}, 201

    @api.response(200, 'OK')
    def get(self):
        """Retrieve list of Users"""
        list_of_users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in list_of_users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
           return {'error': 'User not found'}, 404
        return {'id': user_id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'You cannot modify email or password.')
    @api.response(403, 'Unauthorized action.')
    @jwt_required()
    def put(self, user_id):
        """Update an user's information"""
        # Placeholder for the logic to update a user by ID
        current_user = json.loads(get_jwt_identity())
        user_data = api.payload
        restricted_fields = ['email', 'password']

        if user_id != current_user["id"]:
            return {'error': 'Unauthorized action'}, 403

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
           return {'error': 'Email already registered'}, 400

        if current_user.get("is_admin"):
            restricted_fields = []

        for field in restricted_fields:
            if field in user_data:
                return {'error': 'You cannot modify email or password.'}, 400

        try:
            updated_user = facade.update_user(user_id, user_data)
        except ValueError as error:
            return {'error': 'Invalid input data'}, 400

        if not updated_user:
            return {'error': 'User not found'}, 404
        return {'id': user_id}, 200

    @api.response(200, 'User deleted successfully')
    @api.response(404, 'User not found')
    def delete(self, user_id):
        """Delete a user"""
        user = facade.get_user(user_id)
        if not user:
           return {'error': 'User not found'}, 404
        facade.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200
