#!/usr/bin/python3
import uuid

amenities = ["WiFi", "Swimming Pool", "Air Conditioning"]
for amenity in amenities:
    print(f"INSERT INTO Amenity (id, name) VALUES ('{uuid.uuid4()}', '{amenity}');")
