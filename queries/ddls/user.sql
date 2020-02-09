USE visamo;

CREATE TABLE user(user_id BIGINT PRIMARY KEY, username VARCHAR(20), password VARCHAR(20),first_name VARCHAR(20), last_name VARCHAR(20), phone_number BIGINT, email VARCHAR(50), has_subscribed boolean, is_pro_enabled boolean);

CREATE TABLE `user` (
 `user_id` bigint(20) NOT NULL,
 `username` varchar(20) DEFAULT NULL,
 `password` varchar(20) DEFAULT NULL,
 `first_name` varchar(20) DEFAULT NULL,
 `last_name` varchar(20) DEFAULT NULL,
 `phone_number` bigint(20) DEFAULT NULL,
 `email` varchar(50) DEFAULT NULL,
 `has_subscribed` tinyint(1) DEFAULT NULL,
 `is_pro_enabled` tinyint(1) DEFAULT NULL,
 PRIMARY KEY (`user_id`)
);