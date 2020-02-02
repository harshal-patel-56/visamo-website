USE visamo;

CREATE TABLE user(user_id BIGINT PRIMARY KEY, username VARCHAR(20), password VARCHAR(20),first_name VARCHAR(20), last_name VARCHAR(20), phone_number BIGINT, email VARCHAR(50), has_subscribed boolean, is_pro_enabled boolean);