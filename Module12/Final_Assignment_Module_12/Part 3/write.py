import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# write to server
r.mset({"Milk": "Lactose", "Bread": "Gluten"})