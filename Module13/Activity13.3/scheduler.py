from threading import Timer
import time
import mysqldb
import mongodb
# Uncomment code below for Activity 13.4
#import redisdb
# Uncomment code below for Activity 13.5
# import cassandradb
import sys

# delete data in all dbs
def clearout():
    mysqldb.delete()
    mongodb.delete()
    # call "redisdb.delete()" for Activity 13.4
    # call "cassandradb.delete()" for Activity 13.5
    print('Deleted data in all dbs!')

# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -clear input argument, delete data
if(argument == '-clear'):
    clearout()
    sys.exit()

# -------------
# time loop
# -------------

def status(stamps,db):
    print(f'Data in {db}:')
    for stamp in stamps:
        print(stamp)
    time.sleep(2)

def mysql():
    mysqldb.write()

def mongo():
    stamps = mysqldb.read()
    status(stamps,'mysql')
    mongodb.write(stamps)

# create function redis() for Activity 13.4:
#def redis()

# create function cassandra() for Activity 13.5:
#def cassandra()


def verify():
    stamps = mongodb.read()
    status(stamps,'mongo')
    # call redisdb.read() for Activity 13.4 print results
    # call cassandradb.read() for Activity 13.5 print results

def timeloop():
    print(f'--- LOOP: ' + time.ctime() + ' ---')
    mysql()
    mongo()
    # call function redis() for Activity 13.4
    # call function cassandra() for Activity 13.5
    verify()
    Timer(5, timeloop).start()

timeloop()