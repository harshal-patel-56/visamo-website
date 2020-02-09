USE visamo;

CREATE TABLE property_type(property_type_id INT PRIMARY KEY, property_type_description VARCHAR(20), is_commercial_space boolean);


CREATE TABLE `property_type` (
 `property_type_id` int(11) NOT NULL,
 `property_type_description` varchar(20) DEFAULT NULL,
 `is_commercial_space` tinyint(1) DEFAULT NULL,
 PRIMARY KEY (`property_type_id`)
);