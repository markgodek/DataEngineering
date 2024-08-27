from threading import Timer
import time
import mysqldb
import mongodb
import redisdb
# Uncomment code below for Activity 13.5
# import cassandradb
import sys

# delete data in all dbs
def clearout():
    mysqldb.delete()
    mongodb.delete()
    redisdb.delete()
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
def redis():
    stamps = mysqldb.read();
    redisdb.write(stamps)

# create function cassandra() for Activity 13.5:
#def cassandra()


def verify():
    stamps = mongodb.read()
    status(stamps,'mongo')
    lastInsertDate = redisdb.read()
    print(f'Data in Redis: LastInsertDate = {lastInsertDate.decode("utf-8")}')
    # call cassandradb.read() for Activity 13.5 print results

def timeloop():
    print(f'--- LOOP: ' + time.ctime() + ' ---')
    mysql()
    mongo()
    redis()
    # call function cassandra() for Activity 13.5
    verify()
    Timer(5, timeloop).start()

timeloop()