# Python program killing 
# threads using stop 
# flag tutorial came from https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
  
import threading 
import time 

import Led

led=Led.Led()

def Color(red, green, blue, white = 0):
        """COnvert the provided red, green, blue color to a 24 bit color value.
        Each color component should be a value 0-255 where 0 is the lowest intensity
        and 255 is the highest intensity.
        """
        return (white << 24) | (red << 16)|(green << 8)| blue

def run(stop): 
    while True: 
        print ("Rainbow animation")
        led.rainbow(led.strip)
        led.rainbowCycle(led.strip)
        if stop(): 
            break
                  
def main(): 
        stop_threads = False
        t1 = threading.Thread(target = run, args =(lambda : stop_threads, )) 
        try:
            t1.start() 
        except: 
            print("No thread; sorry")
        i = 0
        for i in range (3):
            print("running main thread")
            time.sleep(1)
        stop_threads = True
        t1.join() 
        print('thread killed') 
        print ("Cleaning up...")
        led.colorWipe(led.strip, Color(0,0,0),10)
main() 