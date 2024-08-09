from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get a database
db = client['employee']

# get collection
employee = db.employee

result = employee.find_one({'LastName': 'Rigby'})

print(result)