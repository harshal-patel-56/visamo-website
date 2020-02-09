USE visamo;

CREATE TABLE image(image_id BIGINT PRIMARY KEY, property_id BIGINT, src_path VARCHAR(100), is_thumbnail boolean);

-- ALTER TABLE image add columns(is_deleted boolean);


CREATE TABLE `image` (
 `image_id` varchar(38) NOT NULL,
 `property_id` varchar(32) DEFAULT NULL,
 `src_path` varchar(100) DEFAULT NULL,
 `is_thumbnail` tinyint(1) DEFAULT NULL,
 PRIMARY KEY (`image_id`)
);