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
