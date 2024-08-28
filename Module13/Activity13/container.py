import os
import sys
import pymysql
import my_sql_container
import my_mongo_container
import my_redis_container
import my_cassandra_container

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root',
        password='Best3tries!',
        host='127.0.0.1')

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    # use db
    query = ("USE pluto")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cursor.execute(query)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()

# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -init, init mysql, mongodb does not need it
if(argument == '-init'):
    init_mysql()
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    my_sql_container.main()
    my_mongo_container.main()
    my_redis_container.main()
    my_cassandra_container.main()
    sys.exit()