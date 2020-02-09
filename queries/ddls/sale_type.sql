USE visamo;

CREATE TABLE sale_type(sale_type_id INT PRIMARY KEY, sale_type_description VARCHAR(20));

CREATE TABLE `sale_type` (
 `sale_type_id` int(11) NOT NULL,
 `sale_type_description` varchar(20) DEFAULT NULL,
 PRIMARY KEY (`sale_type_id`)
);