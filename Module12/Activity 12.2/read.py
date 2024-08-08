from pymongo import MongoClient

# make a connection
client = MongoClient('mongodb://localhost:27017')

# get database
db = client.pluto

# get collection
posts = db.posts

# walk through all posts
for post in posts.find():
    print(post)