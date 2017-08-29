# Create the Arduino service
arduino = Runtime.createAndStart("Arduino","Arduino")
# Connect to the Arduino. Change COM3 to the port where the Arduino is connected
arduino.connect("COM3")
# Start the servo service
servo = Runtime.createAndStart("Servo","Servo")
# Yoy have to change 8 to the pin where your servo is connected
servo.attach(arduino,8)
# Center the servo
servo.setMinMax(10,170)
servo.setRest(90)
servo.rest()
