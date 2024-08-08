from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.pluto

# get collection
posts = db.posts

posts.delete_many({})
