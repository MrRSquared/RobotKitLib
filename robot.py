import pikitlib

#MOTOR PORTS
LEFT = 1
RIGHT = 3
CENTER1 = 2
CENTER2 = 4




class MyRobot():
    def robotInit(self):
        """Robot initialization function"""
        # object that handles basic drive operations
        self.leftBackMotor = pikitlib.SpeedController()
        self.leftFrontMotor = pikitlib.SpeedController()
        self.rightBackMotor = pikitlib.SpeedController()
        self.rightFrontMotor = pikitlib.SpeedController()

        self.left = pikitlib.SpeedControllerGroup(self.leftBackMotor, self.leftFrontMotor)
        self.right = pikitlib.SpeedControllerGroup(self.rightBackMotor, self.rightFrontMotor )

        self.myRobot = pikitlib.DifferentialDrive(self.left, self.right)
       # self.myRobot.setExpiration(0.1)

        self.DEADZONE = 0.4

        #self.driver = wpilib.XboxController(0)
        

    def autonomousInit(self):
        self.myRobot.tankDrive(0.8, 0.8)

    def autonomousPeriodic(self):
        self.myRobot.tankDrive(1, 0.5)

    def teleopInit(self):
        """
        Configures appropriate robot settings for teleop mode
        """
        #self.myRobot.setSafetyEnabled(True)

    def deadzone(self, val, deadzone):
        if abs(val) < deadzone:
            return 0
        return val

    def teleopPeriodic(self):
        #forward = -self.driver.getRawAxis(5) 
        #rotation_value = rotation_value = self.driver.getX(LEFT_HAND)
        forward = 0.7
        rotation_value = 0.2


        forward = self.deadzone(forward, 0.5)

        self.myRobot.arcadeDrive(forward, rotation_value)
