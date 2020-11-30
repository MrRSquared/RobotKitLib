#import time
import sys
import os
import RPi.GPIO as GPIO
class Line_Tracker:
    def __init__(self):
        self.IR01 = 14
        self.IR02 = 15
        self.IR03 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR01,GPIO.IN)
        GPIO.setup(self.IR02,GPIO.IN)
        GPIO.setup(self.IR03,GPIO.IN)
    def getLine(self):
        while True:
            # self.LMR=0x00
            self.line = [0,0,0]
            if GPIO.input(self.IR01)==True:
                self.line[0] = 1
            if GPIO.input(self.IR02)==True:
                self.line[1] = 1
            if GPIO.input(self.IR03)==True:
                self.line[2] = 1
            return self.line
            
infrared=Line_Tracker()
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    while True:
        try:
            print (infrared.getLine())
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program  will be  executed.
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
