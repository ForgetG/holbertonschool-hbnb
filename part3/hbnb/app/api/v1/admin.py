from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services.facade import facade
from flask import request

api = Namespace('admin', description='Admin operations')

@api.route('/users/')
class AdminUserCreate(Resource):
    @api.response(403, 'Admin privileges required')
    @api.response(400, 'Email already registered')
    @api.response(201, 'User created successfully')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')
        is_admin = user_data.get('is_admin', True)

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        user_data['is_admin'] = is_admin
        # Logic to create a new user
        user = facade.create_user(user_data)
        return {'message': 'User created successfully', 'user_id': user.id}, 201

@api.route('/users/<user_id>')
class AdminUserModify(Resource):
    @api.response(403, 'Admin privileges required')
    @api.response(400, 'Email already in use')
    @api.response(200, 'User updated successfully')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')

        # Ensure email uniqueness
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

        # Logic to update user details
        facade.update_user(user_id, data)
        return {'message': 'User updated successfully'}, 200

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @api.response(403, 'Admin privileges required')
    @api.response(201, 'Amenity created successfully')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json
        # Logic to create a new amenity
        amenity = facade.create_amenity(amenity_data)
        return {'message': 'Amenity created successfully', 'amenity_id': amenity.id}, 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @api.response(403,'Admin privileges required')
    @api.response(200, 'Amenity updated successfully')
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = request.json
        # Logic to update an amenity
        facade.update_amenity(amenity_id, amenity_data)
        return {'message': 'Amenity updated successfully'}, 200

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    @api.response(403, 'Unauthorized action')
    @api.response(200, 'Place updated successfully')
    def put(self, place_id):
        current_user = get_jwt_identity()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        place_data = request.json
        # Logic to update the place
        facade.update_place(place_id, place_data)
        return {'message': 'Place updated successfully'}, 200
