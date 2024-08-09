from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get a database
db = client['employee']

# get collection
employee = db.employee

# create a document
employeeCollection = [
                        {"FirstName":"John", "LastName":"Smith", "Age":25},
                        {"FirstName":"Peter", "LastName":"Smith", "Age":26},
                        {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},
                        {"FirstName":"Penny", "LastName":"Lane", "Age":22},
                        {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},
                        {"FirstName":"Helen", "LastName":"Rose", "Age":23}
                     ]
result = employee.insert_many(employeeCollection)

if "employee" in client.list_database_names():

    print("Employee database created!")

print(result.inserted_ids)