import mysql.connector

# DEFAULT MySQL CONNECTION CONFIGURATIONS
HOSTNAME = "localhost"
USERNAME = "root"
PASSWORD = "root"

# DEFAULT DB CONFIGURATIONS
DB_NAME = "visamo"
LOCATIONS_TABLE = "locations"

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
    list_of_fields = ['location_name']
    query = create_query_statement(list_of_fields, LOCATIONS_TABLE)
    print("QUERY    : " + query)
    db_cursor.execute(query)

    list_of_locations = db_cursor.fetchall()

    return list_of_locations
