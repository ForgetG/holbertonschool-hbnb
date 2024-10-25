# HBnB Evolution part2: Business Logic and API Endpoints

In this part we implemented the Business Logic layer and the API Endpoints.


## User Endpoint

    This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for users, while ensuring integration with the Business Logic layer via the Facade pattern.

### User registration

    User model:

        User{
            "first_name"	(string) : "First name of the user"
            "last_name"	(string) : "Last name of the user"
            "email"	(string) : "Email of the user"
        }

    API Response code:

        @api.response(201, 'User successfully created')
        @api.response(400, 'Email already registered')
        @api.response(400, 'Invalid input data')

    CURL tests:

            curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            }'

        Expected Response:

            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            }

        // 201 User successfully created

        Testing invalid data:

            curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
        "first_name": "",
        "last_name": "",
        "email": "invalid-email"
        }'

        Expected Response:

            {
                "error": "Invalid input data"
            }

        // 400 Invalid input data

        Testing Email already registered:

            curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            }'

        Expected Response:

            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            }

        // 201 User successfully created

        curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        }'

        Expected Response:

            {
            "error": "Email already registered"
            }

        // 400 Email already registered

### User get details by id

    API Response code:

        @api.response(200, 'User details retrieved successfully')
        @api.response(404, 'User not found')

    CURL tests:

        GET /api/v1/users/<user_id>
        Content-Type: application/json

        Expected Response:

            {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
            }

        // 200 User details retrieved successfully

        testing invalid user_id:

            GET /api/v1/users/<invalid_user_id>
            Content-Type: application/json

        Expected Response:

            {"error": "User not found"}

        // 404 User not found


### User update

    API Response code:

        @api.response(200, 'User updated successfully')
        @api.response(404, 'User not found')
        @api.response(400, 'Invalid input data')

    CURL tests:

        PUT /api/v1/users/<user_id>
        Content-Type: application/json
        {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        }

        Expected Response:

            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe@example.com"
            }

        // 200 User updated successfully

        testing invalid user_id:

            PUT /api/v1/users/<invalid_user_id>
            Content-Type: application/json

            {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe@example.com"
            }

        Expected Response:

            {"error": "User not found"}

        // 404 User not found

        testing invalid data:

            PUT /api/v1/users/<user_id>
            Content-Type: application/json
    
            {
                "first_name": "",
                "last_name": "",
                "email": "jane.doeexample.com"
            }

        Expected Response:

            {"error": "Invalid input data"}

        // 400 Invalid input data


### User Delete

    API Response code:

        @api.response(200, 'User deleted successfully')
        @api.response(404, 'User not found')

    CURL tests:

        DELETE /api/v1/users/<user_id>
        Content-Type: application/json

        Expected Response:

            {"User deleted successfully"}

        // 200 User deleted successfully

        testing wrong user_id:

            DELETE /api/v1/users/<invalid_user_id>
            Content-Type: application/json

        Expected Response:

            {"error": "User not found"}

        // 404 User not found

## Amenities Endpoint

    This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for users, while ensuring integration with the Business Logic layer via the Facade pattern.

### Amenity Registration

    amenity_model = api.model('Amenity', {
        'name': fields.String(required=True, description='Name of the amenity')
    })

    API Response code:

        @api.response(201, 'Amenity successfully created')
        @api.response(400, 'Invalid input data')

    CURL tests:

        POST /api/v1/amenities/
        Content-Type: application/json

        {
            "name": "Wi-Fi"
        }

        Expected Response:

            {
                "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Wi-Fi"
            }

        // 201 Amenity successfully created

        Testing invalid data:

            POST /api/v1/amenities/
            Content-Type: application/json

            {
                "name": "Wi-Fi"
            }

        Expected Response:

            {"error": "Invalid input data"}

        // 400 Invalid input data


### Retrieve a list of all amenities

    API Response code:

        @api.response(200, 'List of amenities retrieved successfully')

    CURL test:

        GET /api/v1/amenities/
        Content-Type: application/json

        Expected Response:

            [
                {
                    "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "Wi-Fi"
                },
                {
                    "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "Air Conditioning"
                }
            ]

        // 200 List of amenities retrieved successfully


### Update an amenity's information

    API Response code:

        @api.response(200, 'Amenity updated successfully')
        @api.response(404, 'Amenity not found')
        @api.response(400, 'Invalid input data')

    CURL tests:

        PUT /api/v1/amenities/<amenity_id>
        Content-Type: application/json

        {
            "name": "Air Conditioning"
        }

        Expected Response:

            {
                "message": "Amenity updated successfully"
            }

        // 200 Amenity updated successfully


        Testing invalid amenity_id:

            PUT /api/v1/amenities/<invalid_amenity_id>
            Content-Type: application/json

            {
                "name": "Air Conditioning"
            }

            Expected Response:

                {"error": "Amenity not found"}

            // 404 Amenity not found


        Testing invalid data:

            PUT /api/v1/amenities/<amenity_id>
            Content-Type: application/json

            {
                "name": ""
            }

            Expected Response:

                {"error": "Invalid input data"}

            // 400 Invalid input data


### Delete Amenity

    API Response code:

        @api.response(200, 'Amenity deleted successfully')
        @api.response(404, 'Amenity not found')

    CURL Tests:

        DELETE /api/v1/amenities/<amenity_id>
        Content-Type: application/json

        Expected Response:

            {"Amenity deleted succesfully"}

        // 200 Amenity deleted succesfully


        Testing invalid amenity_id:

            DELETE /api/v1/amenities/<invalid_amenity_id>
            Content-Type: application/json

        Expected Response:

            {"error": "Amenity not found}

        // 404 Amenity not found
## Place Endpoint

    This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for places, while ensuring integration with the Business Logic layer via the Facade pattern.


### Place Registration

    Place model:

        place_model = api.model('Place', {
            'title': fields.String(required=True, description='Title of the place'),
            'description': fields.String(description='Description of the place'),
            'price': fields.Float(required=True, description='Price per night'),
            'latitude': fields.Float(required=True, description='Latitude of the place'),
            'longitude': fields.Float(required=True, description='Longitude of the place'),
            'owner_id': fields.String(required=True, description='ID of the owner'),
            'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
        })

    API Response code:

        @api.response(201, 'Place successfully created')
        @api.response(400, 'Invalid input data')

    CURL tests:

        POST /api/v1/places/
        Content-Type: application/json

        {
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }

        Expected Response:

            {
                "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Cozy Apartment",
                "description": "A nice place to stay",
                "price": 100.0,
                "latitude": 37.7749,
                "longitude": -122.4194,
                "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }

        // 201 Place created successfully

        testing invalid data:

            POST /api/v1/places/
            Content-Type: application/json

            {
                "title": "",
                "description": "",
                "price": 100,
                "latitude": 250,
                "longitude": -200,
                "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }

        Expected Response:

            {"error": "Invalid input data}
        
        // 400 Invalid input data



### Place List

    API Response code:

        @api.response(200, 'List of places retrieved successfully')

    CURL test:

        GET /api/v1/places/
        Content-Type: application/json

        Expected Response:

            [
                {
                    "id": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "title": "Cozy Apartment",
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                ...
            ]

        // 200 List of places retrieved successfully



### Update a place's information

    API Response code:

        @api.response(200, 'Place updated successfully')
        @api.response(404, 'Place not found')
        @api.response(400, 'Invalid input data')

    CURL tests:

        PUT /api/v1/places/<place_id>
        Content-Type: application/json

        {
            "title": "Luxury Condo",
            "description": "An upscale place to stay",
            "price": 200.0
        }

        Expected Response:
    
            {
                "message": "Place updated successfully"
            }

        // 200 Place updated succesfully


        Testing invalid place_id:

            PUT /api/v1/places/<invalid_place_id>
            Content-Type: application/json

            {
                "title": "Luxury Condo",
                "description": "An upscale place to stay",
                "price": 200.0
            }

        Expected Response:

            {"error": "Place not found"}
    
        // 404 Place not found


        Testing invalid data:

            PUT /api/v1/places/<place_id>
            Content-Type: application/json

            {
                "title": "",
                "description": "An upscale place to stay",
                "price": abc
            }

        Expected Response:

            {"error": "Invalid input data}
    
        // 400 Invalid input data



### Delete a Place

    API Response code:

        @api.response(200, 'Place deleted successfully')
        @api.response(404, 'Place not found')


    CURL tests:

        DELETE /api/v1/places/<place_id>
        Content-Type: application/json

        Expected Response:

            {"Place deleted succesfully"}

        // 200 Place deleted successfully

        testing Invalid place_id:

            DELETE /api/v1/places/<invalid_place_id>
            Content-Type: application/json

        Expected Response:

            {"error": "Place not found"}

        // 404 Place not found

## Review Endpoint

    This task involves setting up the endpoints to handle CRUD operations (Create, Read, Update) for users, while ensuring integration with the Business Logic layer via the Facade pattern.


### Review Registration

    Review model:

        review_model = api.model('Review', {
            'text': fields.String(required=True, description='Text of the review'),
            'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
            'user_id': fields.String(required=True, description='ID of the user'),
            'place_id': fields.String(required=True, description='ID of the place')
        })


    API Response code:

        @api.response(201, 'Review successfully created')
        @api.response(400, 'Invalid input data')


    CURL tests:

        POST /api/v1/reviews/
        Content-Type: application/json

        {
        "text": "Great place to stay!",
        "rating": 5,
        "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
        }

        Expected Response:

            {
                "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                "text": "Great place to stay!",
                "rating": 5,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
            }

        // 201 Review successfully created


        Testing Invalid data:

            POST /api/v1/reviews/
            Content-Type: application/json

            {
                "text": "",
                "rating": 9,
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "place_id": "1fa85f64-5717-4562-b3fc-2c963f66afa6"
            }

        Expected Response:

            {"error": "Invalid input data"}

        // 400 Invalid input data



### Retrieve All Reviews for a Specific Place

    API Response code:

        @api.response(200, 'List of reviews for the place retrieved successfully')
        @api.response(404, 'Place not found')

    CURL tests:

        GET /api/v1/places/<place_id>/reviews

        Expected Response:

            [
                {
                    "id": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "text": "Great place to stay!",
                    "rating": 5
                },
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "text": "Very comfortable and clean.",
                    "rating": 4
                }
            ]

        // 200 List of reviews for the place retrieved successfully

        Testing Invalid place_id:

            GET /api/v1/places/<invalid_place_id>

        Expected Response:

            {"error": "Place not found"}

        // 404 Place not found 


### Update a review's information

    API Response code:

        @api.response(200, 'Review updated successfully')
        @api.response(404, 'Review not found')
        @api.response(400, 'Invalid input data')


    CURL tests:

        PUT /api/v1/reviews/<review_id>
        Content-Type: application/json

        {
            "text": "Amazing stay!",
            "rating": 4
        }

        Expected Response:

            {
                "message": "Review updated successfully"
            }

        // 200 Review updated successfully


        Testing Invalid review_id:

            PUT /api/v1/reviews/<invalid_review_id>
            Content-Type: application/json

            {
                "text": "Amazing stay!",
                "rating": 4
            }

        Expected Response:

            {"error": "Review not found"}

        // 404 Review not found


        Testing Invalid data:

            PUT /api/v1/reviews/<review_id>
            Content-Type: application/json

            {
                "text": "",
                "rating": -5
            }

        Expected Response:

            {"error": "Invalid input data"}

        // 400 Invalid input data


### Delete Review

    API Response code:

        @api.response(200, 'Review deleted successfully')
        @api.response(404, 'Review not found')

    CURL tests:

        DELETE /api/v1/reviews/<review_id>

        Expected Response:

            {
                "message": "Review deleted successfully"
            }

        // 200 Review deleted successfully


        Testing Invalid review_id:

            DELETE /api/v1/reviews/<invalid_review_id>

        Expected Response:

            {"error": "Review not found"}

        // 404 Review not found

## SWAGGER Documentation

    {
        "definitions": {
            "User": {
                "required": [
                    "email",
                    "first_name",
                    "last_name"
                ],
                "properties": {
                    "first_name": {
                        "type": "string",
                        "description": "First name of the user"
                    },
                    "last_name": {
                        "type": "string",
                        "description": "Last name of the user"
                    },
                    "email": {
                        "type": "string",
                        "description": "Email of the user"
                    }
                },
                "type": "object"
            },
            "Place": {
                "required": [
                    "latitude",
                    "longitude",
                    "owner_id",
                    "price",
                    "title"
                ],
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the place"
                    },
                    "description": {
                        "type": "string",
                        "description": "Description of the place"
                    },
                    "price": {
                        "type": "number",
                        "description": "Price per night"
                    },
                    "latitude": {
                        "type": "number",
                        "description": "Latitude of the place"
                    },
                    "longitude": {
                        "type": "number",
                        "description": "Longitude of the place"
                    },
                    "owner_id": {
                        "type": "string",
                        "description": "ID of the owner"
                    },
                    "amenities": {
                        "type": "array",
                        "description": "List of amenities ID's",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "type": "object"
            },
            "Amenity": {
                "required": [
                    "name"
                ],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the amenity"
                    }
                },
                "type": "object"
            },
            "Review": {
                "required": [
                    "place_id",
                    "rating",
                    "text",
                    "user_id"
                ],
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Text of the review"
                    },
                    "rating": {
                        "type": "integer",
                        "description": "Rating of the place (1-5)"
                    },
                    "user_id": {
                        "type": "string",
                        "description": "ID of the user"
                    },
                    "place_id": {
                        "type": "string",
                        "description": "ID of the place"
                    }
                },
                "type": "object"
            }
        }
    }