import threading
import time
from threading import Timer

titles = ['Harry Potter','Pride and Prejudice']
pages = ['250','430']
first_name = ['J.K.','Jane']
last_name = ['Rowling','Austen']
location = ['UK','UK']

def build_book_dict(titles,pages,first_name,\
                    last_name,location):
   d = {}
   inputs = zip(titles,pages,first_name,last_name,location)
   for titles,pages,first_name,last_name,location in inputs:
      d.update({
         titles:{'Pages':pages,'Author':{'First':first_name,'Last':last_name},
                 'Publisher':{'Location':location}}
      })
   time.sleep(5)
   return d

print(build_book_dict(titles,pages,first_name,last_name,location))

timer = threading.Timer(5,build_book_dict(titles,pages,first_name,last_name,location))
timer.cancel()
print('Timer Cancelled')







def pcde():

   print('This is a course in data engineering.')

#timer = threading.Timer(5.0, pcde)
#timer.start()

#print('Cancelling timer\n')
#timer.cancel()

#print('Exit\n')