from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get a database
db = client['employee']

# get collection
employee = db.employee

filter = {'FirstName':'Helen','LastName':'Rose'}
newValue = {'$set': {'Age':32}}

employee.update_one(filter, newValue)
employeeCursor = employee.find()

for value in employeeCursor:
    print(value)