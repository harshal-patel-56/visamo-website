import mysql.connector

# DEFAULT MySQL CONNECTION CONFIGURATIONS
HOSTNAME = "localhost"
USERNAME = "root"
PASSWORD = ""

# DEFAULT DB CONFIGURATIONS
DB_NAME = "visamo"
LOCATIONS_TABLE = "location"
PROPERTY_TYPES_TABLE = "property_type"
SALE_TYPES_TABLE = "sale_type"

# CONNECTION TO DB
db = mysql.connector.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, database=DB_NAME)

# DB_CURSOR OBJECT
db_cursor = db.cursor()


# Generic function to create a select query
def create_query_statement(fields, table_name, conditional_expression=""):
    column_names = ','.join(fields)
    return "SELECT " + column_names + " FROM " + table_name + conditional_expression + ";"


# Method to fetch all the locations from DB
def get_locations():
    list_of_fields = ['location_id','location_name']
    query = create_query_statement(list_of_fields, LOCATIONS_TABLE)
    # print("QUERY    : " + query)
    db_cursor.execute(query)

    list_of_locations = db_cursor.fetchall()

    return list_of_locations

# Method to fetch all the properties types from DB
def get_property_types():
    list_of_fields = ['property_type_id','property_type_description']
    query = create_query_statement(list_of_fields, PROPERTY_TYPES_TABLE)
    # print("QUERY    : " + query)
    db_cursor.execute(query)

    list_of_property_types = db_cursor.fetchall()

    return list_of_property_types

# Method to fetch all the sale types from DB
def get_sale_types():
    list_of_fields = ['sale_type_id','sale_type_description']
    query = create_query_statement(list_of_fields, SALE_TYPES_TABLE)
    # print("QUERY    : " + query)
    db_cursor.execute(query)

    list_of_sale_types = db_cursor.fetchall()

    return list_of_sale_types

# Method to fetch all the Properties from DB to render on index page
def get_all_properties():
    query = """SELECT
                    property_name,
                    property_type_description,
                    location_name,
                    sale_type_description,
                    price,
                    area,
                    src_path,
                    p.property_id
                    FROM
                    property p
                    JOIN location l ON p.location_id = l.location_id
                    JOIN sale_type st ON p.sale_type_id = st.sale_type_id
                    JOIN image img ON p.property_id = img.property_id
                    JOIN property_type ON p.property_type_id = property_type.property_type_id
                    WHERE is_approved AND is_available AND is_thumbnail;"""
    db_cursor.execute(query)
    list_of_all_properties = db_cursor.fetchall()
    return list_of_all_properties

# Method to fetch all the Properties from DB to render on index page
def get_requested_properties(LOCATION_ID, PROPERTY_TYPE, SALE_TYPE, GT_PRICE, LW_PRICE):
    query = f"""SELECT
                    property_name,
                    property_type_description,
                    location_name,
                    sale_type_description,
                    price,
                    area,
                    src_path,
                    p.property_id
                    FROM
                    property p
                    JOIN location l ON p.location_id = l.location_id
                    JOIN sale_type st ON p.sale_type_id = st.sale_type_id
                    JOIN image img ON p.property_id = img.property_id
                    JOIN property_type ON p.property_type_id = property_type.property_type_id
                    WHERE is_approved AND is_available AND is_thumbnail
                    AND p.price <= {GT_PRICE} AND p.price >= {LW_PRICE}
                    AND l.location_id = {LOCATION_ID}
                    AND st.sale_type_id = {SALE_TYPE}
                    AND p.property_type_id = {PROPERTY_TYPE}"""
    db_cursor.execute(query)
    list_of_all_properties = db_cursor.fetchall()
    return list_of_all_properties

# Method to fetch all the info of Property
def get_property_info(PROPERTY_ID):
    query = f"""SELECT
                    property_name,
                    description,
                    property_type_description,
                    property_address,
                    location_name,
                    city,
                    state,
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
                    WHERE is_available AND is_thumbnail
                    AND p.property_id = '{PROPERTY_ID}'"""
    db_cursor.execute(query)
    propertie_info = db_cursor.fetchall()
    return propertie_info

# Method to fetch all the Properties from DB to render on index page
def get_pending_properties():
    query = """SELECT
                    property_name,
                    property_type_description,
                    location_name,
                    sale_type_description,
                    price,
                    area,
                    src_path,
                    p.property_id
                    FROM
                    property p
                    JOIN location l ON p.location_id = l.location_id
                    JOIN sale_type st ON p.sale_type_id = st.sale_type_id
                    JOIN image img ON p.property_id = img.property_id
                    JOIN property_type ON p.property_type_id = property_type.property_type_id
                    WHERE is_approved = 0 AND is_available AND is_thumbnail;"""
    db_cursor.execute(query)
    list_of_pending_properties = db_cursor.fetchall()
    return list_of_pending_properties

def insert_property(property_id, user_id, property_name, property_description, address, price, location, property_type,
                    sale_type, area, age, is_owner, src_path):
    address = address.replace("'","\\\'")
    query = f"""INSERT INTO `property` (`property_id`, `user_id`, `property_name`, `description`, `property_address`, `price`, `location_id`, `property_type_id`, `sale_type_id`, `area`, `ageing`, `is_owner`, `is_featured`, `is_available`, `is_approved`, `created`) 
                VALUES ('{property_id}', '{user_id}', '{property_name}', '{property_description}', '{address}', '{price}', '{location}', '{property_type}', '{sale_type}', '{area}', '{age}', '{is_owner}', '0', '1', '0', CURRENT_TIMESTAMP)"""


    db_cursor.execute(query)
    db.commit()

    query = f"""INSERT INTO `image` (`image_id`, `property_id`, `src_path`, `is_thumbnail`) VALUES ('{property_id}', '{property_id}', '{src_path}', '1')"""
    db_cursor.execute(query)

    db.commit()
    return True


def approve(PROPERTY_ID):
    query = f"""UPDATE `property` SET is_approved = 1 WHERE property_id = '{PROPERTY_ID}'"""

    db_cursor.execute(query)
    db.commit()
    return True

# def add_user():
