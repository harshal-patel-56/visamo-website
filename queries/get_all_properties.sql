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
JOIN location l ON p.property_id = l.location_id
JOIN sale_type st ON p.sale_type_id = st.sale_type_id
JOIN image img ON p.property_id = img.property_id
WHERE is_approved AND is_available AND is_thumbnail;