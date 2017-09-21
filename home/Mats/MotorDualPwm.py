# Start the services
ard = Runtime.start("ard","Arduino")
vard = Runtime.start("vard","VirtualArduino")
ada = Runtime.start("ada","Adafruit16CServoDriver")
motor = Runtime.create("motor","MotorDualPwm")
vard.connect ("COM99")
ard.connect("COM99")
ada.attach("ard","0","0x40")
motor.setLeftPwmPin(0);
motor.setRightPwmPin(1);
motor.attach(ard)
