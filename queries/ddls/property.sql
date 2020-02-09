USE visamo;

CREATE TABLE property(property_id BIGINT PRIMARY KEY, user_id BIGINT, property_name VARCHAR(50), description VARCHAR(100), price DOUBLE, location_id INT, sale_type_id INT, area DOUBLE, ageing INT, is_owner boolean, is_featured boolean, is_available boolean, is_approved boolean, created TIMESTAMP);

CREATE TABLE `property` (
 `property_id` varchar(32) NOT NULL,
 `user_id` bigint(20) DEFAULT NULL,
 `property_name` varchar(50) DEFAULT NULL,
 `description` varchar(200) DEFAULT NULL,
 `property_address` text NOT NULL,
 `price` double DEFAULT NULL,
 `location_id` int(11) DEFAULT NULL,
 `property_type_id` int(11) NOT NULL,
 `sale_type_id` int(11) DEFAULT NULL,
 `area` double DEFAULT NULL,
 `ageing` int(11) DEFAULT NULL,
 `is_owner` tinyint(1) DEFAULT NULL,
 `is_featured` tinyint(1) DEFAULT NULL,
 `is_available` tinyint(1) DEFAULT NULL,
 `is_approved` tinyint(1) DEFAULT '0',
 `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY (`property_id`)
);
