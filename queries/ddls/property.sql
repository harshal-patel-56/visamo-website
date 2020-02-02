USE visamo;

CREATE TABLE property(property_id BIGINT PRIMARY KEY, user_id BIGINT, description VARCHAR(100), price DOUBLE, location_id INT, sale_type_id INT, area DOUBLE, ageing INT, is_owner boolean, is_featured boolean, is_available boolean, is_approved boolean, created TIMESTAMP);