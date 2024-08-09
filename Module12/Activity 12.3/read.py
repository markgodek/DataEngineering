# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items
#for item in r.lrange('nums', 0, -1):
#    print(item)

# get value based on key
capitalOfItaly = r.get('Italy')
print('Capital of Italy: ', capitalOfItaly)

# print all key-value pairs
keys = r.keys()
for key in keys:
    print('Key:', key,'-','Value:',r.get(key))

# clean up from the boilerplate code
#r.delete('nums')