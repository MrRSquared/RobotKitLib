# Python program killing 
# threads using stop 
# flag 
  
import threading 
import time 
  
def run(stop): 
    while True: 
        print('thread running')
        time.sleep(2) 
        if stop(): 
                break
                  
def main(): 
        stop_threads = False
        t1 = threading.Thread(target = run, args =(lambda : stop_threads, )) 
        try:
            t1.start() 
            time.sleep(5)
            stop_threads = True
            t1.join() 
            print('thread killed') 
        except KeyboardInterrupt:
            stop_threads = True
            t1.join() 
            print('thread killed') 
main() 