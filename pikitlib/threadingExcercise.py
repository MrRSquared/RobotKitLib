# Python program creating 
# three threads 

import threading 
import time

def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')

stop_threads = False
# counts from 1 to 9 
def func(): 
	while True:
		for i in range(1, 10): 
			time.sleep(0.001) 
			#print('Thread ' + str(number) + ': prints ' + str(number*i)) 
			print("hi"+str(i))
		if stop_threads:
			print("ending")
			break

# creates 3 threads 
# for i in range(0,3): 
thread = threading.Thread(target=func, daemon =True) 
thread.start() 
time.sleep(3)
stop_threads = True
thread.join() 
print('thread killed')
time.sleep(1)
print("exiting")
