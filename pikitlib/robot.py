#Ultrasonic Robot.py
import pikitlib
import time
from networktables import NetworkTables
# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

import robotmap
import Led
import UltraSonic
import Line_Tracker

LEFT_HAND = 1
RIGHT_HAND = 0

class MyRobot():
    def robotInit(self):
        """Robot initialization function"""
        # object that handles basic drive operations
        self.leftBackMotor = pikitlib.SpeedController(robotmap.BACK_LEFT)
        self.leftFrontMotor = pikitlib.SpeedController(robotmap.FRONT_LEFT)
        self.rightBackMotor = pikitlib.SpeedController(robotmap.BACK_RIGHT)
        self.rightFrontMotor = pikitlib.SpeedController(robotmap.FRONT_RIGHT)

        self.left = pikitlib.SpeedControllerGroup(self.leftBackMotor, self.leftFrontMotor)
        self.right = pikitlib.SpeedControllerGroup(self.rightBackMotor, self.rightFrontMotor )

        self.myRobot = pikitlib.DifferentialDrive(self.left, self.right)
        self.ultrasonic = UltraSonic.UltraSonic()
        self.led = Led.Led()
        self.line = Line_Tracker.Line_Tracker()
       # self.myRobot.setExpiration(0.1)

        self.DEADZONE = 0.4

        #self.buzz = pikitlib.IllegalBuzzer()

        NetworkTables.initialize()
        self.driver = pikitlib.XboxController(0)
    def disabledInit(self):
        self.led.colorWipeSolid(self.led.strip, (0,0,0))


    def autonomousInit(self):
        #self.myRobot.tankDrive(0.8, 0.8)
        logging.debug("Entering auto.")

    def autonomousPeriodic(self):
        #self.myRobot.tankDrive(1, 0.5)
        #self.led.colorWipeSolid(self.led.strip, (50,0,50))
        distance = self.ultrasonic.get_distance()
        logging.debug(distance)
        if distance > 50:
            self.led.colorWipeSolid(self.led.strip, (0,50,0))
        if distance < 50:
            self.led.colorWipeSolid(self.led.strip, (50,0,0))
    def teleopInit(self):
        """
        Configures appropriate robot settings for teleop mode
        """
        self.left.setInverted(False)
        self.right.setInverted(False)
        
    def deadzone(self, val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val

    def teleopPeriodic(self):
        print(self.line.getLine())
        
        '''forward = self.driver.getX(LEFT_HAND)
        forward = 0.80 * self.deadzone(forward, robotmap.DEADZONE)
        rotation_value = -0.8 * self.driver.getY(RIGHT_HAND)
        self.myRobot.arcadeDrive(forward,rotation_value)'''
