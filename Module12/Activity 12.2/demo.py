import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['mydatabase']

print(myclient.list_database_names())

mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

mycol.insert_one(mydict)
print(mydb.list_collection_names())

mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

customers = mydb.customers

for customer in customers.find():
    print(customer)

customers.delete_many({})

for customer in customers.find():
    print(customer)
print('done')