USE visamo;

CREATE TABLE location(location_id INT PRIMARY KEY, location_name VARCHAR(20), landmark VARCHAR(20), city VARCHAR(20), state VARCHAR(20), country VARCHAR(20));


CREATE TABLE `location` (
 `location_id` int(11) NOT NULL,
 `location_name` varchar(20) DEFAULT NULL,
 `landmark` varchar(20) DEFAULT NULL,
 `city` varchar(20) DEFAULT NULL,
 `state` varchar(20) DEFAULT NULL,
 `country` varchar(20) DEFAULT NULL,
 PRIMARY KEY (`location_id`)
);