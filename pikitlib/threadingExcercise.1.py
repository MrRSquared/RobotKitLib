# Python program killing 
# thread using daemon 

# Python program killing 
# threads using stop 
# flag 
  
import threading 
import time
import sys

def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')
  
def run(stop): 
    while True: 
        print('thread running') 
        if stop(): 
                break
                  
def main(): 
       
        stop_threads = False
        t1 = threading.Thread(target = run, args =(lambda : stop_threads, )) 
        t1.start() 
        time.sleep(1) 
        stop_threads = True
        t1.join() 
        print('thread killed')
                 
main()
sys.exit() 

  
 
