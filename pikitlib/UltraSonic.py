import os
import sys
import time
import threading
# TODO: create its own thread because we want this to be an interrupt.
import RPi.GPIO as GPIO
class UltraSonic:
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)
        self.currentDistance = 0
        self.distance_thread()
    def send_trigger_pulse(self):
        GPIO.output(self.trigger_pin,True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin,False)

    def wait_for_echo(self,value,timeout):
        count = timeout
        while GPIO.input(self.echo_pin) != value and count>0:
            count = count-1
    
    def distance_thread(self):
        thread = threading.Thread(target=self.distanceLoop, daemon =True)
        thread.start()
        
    
     
    def measure_distance(self):
        oldDistance = 0
        distance_cm=[0,0,0,0,0]
        for i in range(3):
            self.send_trigger_pulse()
            self.wait_for_echo(True,10000)
            start = time.time()
            self.wait_for_echo(False,10000)
            finish = time.time()
            pulse_len = finish-start
            distance_cm[i] = pulse_len/0.000058
        distance_cm=sorted(distance_cm)
        
        if distance_cm[2] < .001 :
            distance_cm[2] = oldDistance
        else:
            oldDistance = distance_cm[2]
        return int(distance_cm[2])
    def distanceLoop(self):
        while True:
            self.currentDistance = self.measure_distance()
    def get_distance(self):
        return self.currentDistance
             
# Main program logic follows:
if __name__ == '__main__':
    ultrasonic=UltraSonic() 
    print ('Program is starting ... ')
    while True:
        try:
            m = ultrasonic.get_distance()
            print(m)

        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)