# Python program killing 
# threads using stop 
# flag tutorial came from https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
  
import threading 
import time 
import Led
import signal
import sys

led=Led.Led()

def Color(red, green, blue, white = 0):
    """Convert the provided red, green, blue color to a 24 bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (white << 24) | (red << 16)|(green << 8)| blue


def goodbye(name, adjective):
    led.colorWipe(led.strip, Color(0,0,0),10)
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')

stop_threads = False
# counts from 1 to 9 
def func():
    count = 0; 
    while True:
        print ("Rainbow animation")
        led.colorWipe(led.strip, Color(20,0,count+1),10)
        count+=1
        if count>255:
            count = 0
        if stop_threads:
            print("ending")
            break

# creates 3 threads
#for i in range(0): 
thread = threading.Thread(target=func, daemon =True) 
thread.start() 
time.sleep(3)
stop_threads = True
thread.join() 
print('thread killed')
time.sleep(1)
print("exiting")