DROP TABLE IF EXISTS Amenity;

CREATE TABLE Amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

INSERT INTO Amenity (id, name) VALUES ('06283467-5c2a-4d2f-898d-363cafebc8d5', 'WiFi');
INSERT INTO Amenity (id, name) VALUES ('9544c114-8a61-454c-8172-d3d3a21886c4', 'Swimming Pool');
INSERT INTO Amenity (id, name) VALUES ('4d47e91f-fa80-4a40-99e2-b4d488923007', 'Air Conditioning');
