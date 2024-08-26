import os
import sys

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3306:3306 --name some-mysql \
    -e MYSQL_ROOT_PASSWORD=Best3tries! -d mysql','mysql')
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongo')
    create('docker run -p 6379:6379 --name some-redis -d redis','redis')
    create('docker run -p 9042:9042 --name some-cassandra -d cassandra', 'cassandra')
# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')
    delete('some-cassandra')