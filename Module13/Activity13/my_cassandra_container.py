import os
import sys

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

def main():
    # read input argument
    argument = len(sys.argv)
    if (argument > 1):
        argument = sys.argv[1]

    if(argument == '-create'):
        create('docker run -p 1000:1000 --name final_cassandra_container -d cassandra', 'cassandra')