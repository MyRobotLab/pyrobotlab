# Start the Adafruit16CServodriver that can be used for all PCA9685 devices
adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver")
#
# This part of the script is for the Arduino
# Comment it out or delete it if you use the GPIO pins of the Raspberry PI
# Change COM4 to the port where your Arduino is connected
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM4")
adaFruit16c.setController("Arduino","1","x040")
#
# This part of the script is if you use the GPOI pins of the Raspberry PI
# Comment it out or delete it if you use an Arduino
raspi = Runtime.createAndStart("RasPi","RasPi")
adaFruit16c.setController("RasPi","1","x040")
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
