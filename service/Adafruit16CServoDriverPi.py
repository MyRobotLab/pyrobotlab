# From version 1.0.2316 use attach instead of setController
# This script is if you use the GPOI pins of the Raspberry PI
raspi = Runtime.createAndStart("RasPi","RasPi")
# adaFruit16c.setController("RasPi","1","0x40")
adaFruit16c.attach("RasPi","1","0x40")
#
# This part is common for both devices and creates two servo instances
# on port 3 and 8 on the Adafruit16CServoDriver
# Change the names of the servos and the pin numbers to your usage
thumb = Runtime.createAndStart("Thumb", "Servo")
elbow = Runtime.createAndStart("Elbow", "Servo")
# attach it to the pwm board - pin 3 & 8
thumb.attach(adaFruit16c,3)
elbow.attach(adaFruit16c,8)
# When this script has been executed you should be able to 
# move the servos using the GUI or using python
