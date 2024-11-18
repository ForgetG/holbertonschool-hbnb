DROP TABLE IF EXISTS Review;

CREATE TABLE Review (
    id CHAR(36) PRIMARY KEY,
    text TEXT,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    user_id CHAR(36) NOT NULL,
    place_id CHAR(36) NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES User(id),
    CONSTRAINT fk_place FOREIGN KEY (place_id) REFERENCES Place(id),
    CONSTRAINT unique_user_place UNIQUE (user_id, place_id)
);
