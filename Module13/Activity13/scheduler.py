from threading import Timer
import time
import mysqldb
import mongodb

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

def verify():
    stamps = mongodb.read()
    status(stamps,'mongo')


def timeloop():
    print(f'--- LOOP: ' + time.ctime() + ' ---')
    mysql()
    mongo()
    verify()
    Timer(5, timeloop).start()

timeloop()