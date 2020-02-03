USE visamo;

SELECT
property_name,
location_name,
sale_type_description,
price,
area,
src_path
FROM
property p
JOIN location l ON p.location_id = l.location_id
JOIN sale_type st ON p.sale_type_id = st.sale_type_id
JOIN image img ON p.property_id = img.property_id
WHERE is_approved AND is_available AND is_thumbnail
AND p.price <= GT_PRICE AND p.price >= LW_PRICE
AND l.location_id = LOC_ID
AND st.sale_type_id = SALE_TYPE
AND p.property_type = PROPERTY_TYPE;

# version 2

SELECT
property_name,
property_type_description,
location_name,
sale_type_description,
price,
area,
src_path
FROM
property p
JOIN location l ON p.location_id = l.location_id
JOIN sale_type st ON p.sale_type_id = st.sale_type_id
JOIN image img ON p.property_id = img.property_id
JOIN property_type ON p.property_type_id = property_type.property_type_id
WHERE is_approved AND is_available AND is_thumbnail
AND p.price <= GT_PRICE AND p.price >= LW_PRICE
AND l.location_id = LOC_ID
AND st.sale_type_id = SALE_TYPE
AND p.property_type = PROPERTY_TYPE