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

# Method to fetch all the property types from DB
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
                    src_path
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
                    src_path
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