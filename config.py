import pymongo

client = pymongo.MongoClient("mongodb+srv://harshal_56:root12345@visamo-cluster-iid18.mongodb.net/test?retryWrites=true&w=majority")
db_list = client.list_database_names()

db = client["visamo_db"]
# cluster_list = db.list_collection_names()
collection = db["properties"]

# property_info = {
#                     "location"  : "Gorwa",
#                     "type"      : "Farm House",
#                     "price"     : "250000",
#                     "bedrooms"  : "4",
#                     "bathrooms" : "3",
#                     "for"       : "Rent"
#                 }

# x = collection.insert_one(property_info)

# print(x.inserted_id)

# query = { '$and': [ { 'price': { '$gt': 100000 } }, { 'price': { '$lt': 5000000 } } ] }
#
# res = collection.find(query)
# for x in res:
#     print(x)