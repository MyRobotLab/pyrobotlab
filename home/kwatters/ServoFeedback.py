###################################################
# ServoFeedback.py
# This script shows how to use analog feedback
# from the potentiometer of a hobby servo
# to determine the servos actual angle
# In this example we're using an Arduino Uno
# The Servo is connected to digital pin 8 of the Arduino
# The supply voltage (red wire on potentiometer) is connected to Vref  
# The center pin on the potentiometer is connected to A0 
# Note: ground was not connected from the potentiometer
# as it was observed that the potentiometer 3rd pin is not actually at ground.

###################################################
# Read the pin data in a callback from the arduino
# if it's pin 0, this is 
###################################################
def pinData(pin):
  centerValue = 550  
  resolution = 4.3
  if pin.pin == 0:
    #  print str(pin.value) + " " +str(pin.type) + " " + str(pin.pin)
    print str(pin.value) + " " + str(pin.pin)
    # the pin value will be between 0-1023 center is at 550 (usually)
    # 90 degrees is measured as 550 and 100 degrees is 593.
    # get the difference from 90 degrees
    diff = pin.value - centerValue
    # how big is that difference in degrees
    delta = diff/resolution
    angle = 90 + delta
    print "Measured angle is " + str(angle)
    # TODO: servo.moveTo(angle)
    

# Create the arduino
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM30")
# create and attach the servo
servo = Runtime.createAndStart("servo", "Servo")
servo.attach("arduino", 8)

# add the python call back for the publishPin method to invok pinData in python.
arduino.addListener("publishPin", "python", "pinData")

# start reading the value from analog pin 0.
arduino.analogReadPollingStart(0)

# move the servo to center position  (here, I used the GUI and measured 550)
# this computes the center value
# use the gui to move the angle +/- 10 degrees to another angle and compute the resolution.
# update the constants in the pinData method
servo.moveTo(90)

# TODO: programmatically implement the calibration methods.



