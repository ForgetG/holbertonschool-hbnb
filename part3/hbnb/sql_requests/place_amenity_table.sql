DROP TABLE IF EXISTS Place_Amenity;

CREATE TABLE Place_Amenity (
    place_id CHAR(36) NOT NULL,
    amenity_id CHAR(36) NOT NULL,
    CONSTRAINT fk_place FOREIGN KEY (place_id) REFERENCES Place(id),
    CONSTRAINT fk_amenity FOREIGN KEY (amenity_id) REFERENCES Amenity(id),
    PRIMARY KEY (place_id, amenity_id)
);