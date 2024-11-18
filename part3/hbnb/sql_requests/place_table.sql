DROP TABLE IF EXISTS Place;

CREATE TABLE Place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36) NOT NULL,
    CONSTRAINT fk_owner FOREIGN KEY (owner_id) REFERENCES User(id)
);