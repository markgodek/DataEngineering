import threading
from threading import Timer

def pcde():

   print('This is a course in data engineering.')

timer = threading.Timer(5.0, pcde)
timer.start()

print('Cancelling timer\n')
timer.cancel()

print('Exit\n')