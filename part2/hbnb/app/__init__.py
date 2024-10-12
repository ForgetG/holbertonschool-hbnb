#!/usr/bin/python3
"""Module app importable package
"""
from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    
    # Placeholder for API namespaces (endpoints will be added later)
    # Additionnal namespaces for places, reviews, and amenities will be added later
    
    return app
