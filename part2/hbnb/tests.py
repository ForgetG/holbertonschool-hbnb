#!/usr/bin/python3
"""Module tests
"""
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response_user.status_code, 201)    

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])

    def test_get_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe5@example.com"
            })
        user_id = response_user.get_json()['id']

        response_updated_user = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "Jone",
            "last_name": "Dol",
            "email": "jone.dole@example.com"
        })
        self.assertEqual(response_updated_user.status_code, 200)

    def test_delete_user(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe6@example.com"
            })
        user_id = response_user.get_json()['id']

        response_user = self.client.delete(f'/api/v1/users/{user_id}')
        self.assertEqual(response_user.status_code, 200)

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_data(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])

    def test_get_amenities(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_update_amenity(self):
        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi1"
        })
        amenity_id = response_amenity.get_json()['id']

        response_updated_amenity = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Wifi2"
        })
        self.assertEqual(response_updated_amenity.status_code, 200)

    def test_delete_amenity(self):
        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi3"
        })
        amenity_id = response_amenity.get_json()['id']

        response_amenity = self.client.delete(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response_amenity.status_code, 200)


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        response_user = self.client.post('/api/v1/users/', json={
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe2@example.com"
            })
        user_id = response_user.get_json()['id']

        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        amenity_id = response_amenity.get_json()['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "House",
            "description": "Beautiful house",
            "price": 100.50,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_data(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": 100.50,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": "1",
            "amenities": ["1"]
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])

    def test_get_places(self):
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_update_place(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe7@example.com"
            })
        user_id = response_user.get_json()['id']

        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        amenity_id = response_amenity.get_json()['id']

        response_place = self.client.post('/api/v1/places/', json={
            "title": "House",
            "description": "Beautiful house",
            "price": 100.50,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        place_id = response_place.get_json()['id']

        response_updated_place = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "Small house",
            "description": "Ugly house",
            "price": 25.40,
            "latitude": 38.7749,
            "longitude": -120.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        self.assertEqual(response_updated_place.status_code, 200)

    def test_delete_place(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe9@example.com"
        })
        user_id = response_user.get_json()['id']

        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        amenity_id = response_amenity.get_json()['id']

        response_place = self.client.post('/api/v1/places/', json={
            "title": "Apartement",
            "description": "Social house",
            "price": 120.50,
            "latitude": 38.7749,
            "longitude": -112.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        place_id = response_place.get_json()['id']

        response_place = self.client.delete(f'/api/v1/places/{place_id}')
        self.assertEqual(response_place.status_code, 200)

class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response_user = self.client.post('/api/v1/users/', json={
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane.doe76@example.com"
            })
        user_id = response_user.get_json()['id']

        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi4"
        })
        amenity_id = response_amenity.get_json()['id']

        response_place = self.client.post('/api/v1/places/', json={
            "title": "House",
            "description": "Beautiful house",
            "price": 100.50,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        place_id = response_place.get_json()['id']

        response_review = self.client.post('/api/v1/reviews/', json={
            "text": "Great place",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response_review.status_code, 201)

    def test_create_review_invalid_data(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "rating": 5,
            "user_id": "1",
            "place_id": "1"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid input data', response.get_json()['error'])

    def test_get_reviews(self):
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jacques",
            "last_name": "Delanoe",
            "email": "jacques.delanoe@example.com"
        })
        print(response_user.get_json())
        user_id = response_user.get_json()['id']
        print(user_id)

        response_amenity = self.client.post('/api/v1/amenities/', json={
            "name": "Wifi"
        })
        amenity_id = response_amenity.get_json()['id']

        response_place = self.client.post('/api/v1/places/', json={
            "title": "Household",
            "description": "Beautiful household",
            "price": 101.50,
            "latitude": 45.7749,
            "longitude": -98.4194,
            "owner_id": user_id,
            "amenities": [amenity_id]
        })
        place_id = response_place.get_json()['id']

        response_review = self.client.post('/api/v1/reviews/', json={
            "text": "Great place",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        self.assertEqual(response_review.status_code, 201)

    def test_delete_review(self):
        response_user = self.client.post('/api/v1/users/', json={
            "first_name": "Jack",
            "last_name": "Attali",
            "email": "jack.attali@example.com"
        })
        user_id = response_user.get_json()['id']

        response_place = self.client.post('/api/v1/places/', json={
            "title": "HOPLITO",
            "description": "DIOGINOS",
            "price": 108.50,
            "latitude": 49.7749,
            "longitude": -97.4194,
            "owner_id": user_id,
            "amenities": []
        })
        place_id = response_place.get_json()['id']

        response_review = self.client.post(f'/api/v1/reviews/', json={
            "text": "Great place",
            "rating": 5,
            "user_id": user_id,
            "place_id": place_id
        })
        print(response_review.get_json())
        review_id = response_review.get_json()['id']

        response_review = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response_review.status_code, 200)


if __name__ == '__main__':
    unittest.main()
