# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# print all key-value pairs
keys = r.keys()
for key in keys:
    print('Key:', key,'-','Value:',r.get(key))