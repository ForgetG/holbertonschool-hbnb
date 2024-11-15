#!/usr/bin/python3
"""Module app importable package
"""
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.admin import api as admin_ns

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namepsace
    api.add_namespace(users_ns, path='/api/v1/users')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Register the authentification namespace
    api.add_namespace(auth_ns, path='/api/v1/auth')

    # Register the administrator namespace
    api.add_namespace(admin_ns, path='/api/v1/admin')

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    return app
