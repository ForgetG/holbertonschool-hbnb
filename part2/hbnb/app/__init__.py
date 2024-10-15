#!/usr/bin/python3
"""Module app importable package
"""
from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Register the users namepsace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Additionnal namespaces for places, reviews, and amenities will be added later
    return app
