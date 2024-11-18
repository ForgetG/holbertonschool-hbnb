DROP TABLE IF EXISTS User;

CREATE TABLE User (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

INSERT INTO User (id, email, first_name, last_name, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', 
    'admin@hbnb.io', 
    'Admin', 
    'HBnB', 
    '$2b$12$k4Fsb4BJIBUr76AALeN3OufOeCWnvSMsIQ3RYJ8I1Dr9AoHWn7q2i', 
    TRUE
);
