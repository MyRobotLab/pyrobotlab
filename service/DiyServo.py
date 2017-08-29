<<<<<<< HEAD
# This is a demo of the setup for DiyServo. 
# This setup is valid from version 1.0.2274
# The difference compared to earlier versions is that it now
# starts a MotorDualPwm service that connects to the Arduino
# Before the DiyServo connected directly to the Arduino.
#
# Start of script for DiyServo
# Analog input A0 is the same as digital 14 on the Arduino Uno  
A0 = 14
# Start the Arduino 
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM3")
# Start the MotorDualPwm. You can use also use a different type of Motor
motor = Runtime.createAndStart("diyservo.motor","MotorDualPwm")
# Tell the motor to attach to the Arduino and what pins to use
motor.attach(arduino)
motor.setPwmPins(10,11)
# Start the DiyServo
servo = Runtime.createAndStart("diyservo","DiyServo")
servo.attach(arduino,A0) # Attach the analog pin 0 
servo.moveTo(90)
# At this stage you can use the gui or a script to control the DiyServo
=======
# webgui = Runtime.createAndStart("webgui","WebGui")
# Start of script for DiyServo
# Analog input A0 is the same as digital 14 on the Arduino Uno  
A0 = 14
# Start the Arduino
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM3")
# Start Servo
servo = Runtime.createAndStart("Servo","DiyServo")
servo.setPwmPins(10,11)
servo.attach(arduino)      # Attach the motorcontroller
servo.attach(arduino,A0) # Attach the analog pin 0 
servo.moveTo(90)
# End of script for DiyServo
>>>>>>> master
