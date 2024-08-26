import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='Best3tries!',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `bikes`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS bikes")
cursor.execute(query)

# use db
query = ("USE bikes")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE brands(
    id VARCHAR(36),
    name VARCHAR(20)
)
''')
cursor.execute(query)

inserts = [f'INSERT INTO `brands` VALUES("1","Specialized")',
           f'INSERT INTO `brands` VALUES("2","Trek")',
           f'INSERT INTO `brands` VALUES("3","Giant")']

for command in inserts:
    cursor.execute(command)

query = ("SELECT * FROM brands")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cnx.commit()
cursor.close()
cnx.close()    