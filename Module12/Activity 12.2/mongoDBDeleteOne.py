from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get a database
db = client['employee']

# get collection
employee = db.employee

filter = {'LastName': 'Rose'}
employee.delete_one(filter)

employeeCursor = employee.find()
for value in employeeCursor:
    print(value)