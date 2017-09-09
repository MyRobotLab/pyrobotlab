# This example shows how to use the Adafruit16CServoDriver 
# It can be used with Arduino, RasPi or Esp8266_01
# From version 1.0.2316 use attach instead of setController
# 
# Start the Adafruit16CServodriver that can be used for all PCA9685 devices
adaFruit16c = Runtime.start("AdaFruit16C","Adafruit16CServoDriver")
#
# This part of the script is for the Arduino
# Comment it out the three lines below if you don't use the Arduino
# Change COM4 to the port where your Arduino is connected
arduino = Runtime.start("arduino","Arduino")
arduino.connect("COM3")
adaFruit16c.attach("arduino","0","0x40")
#
# This part of the script is if you use the GPOI pins of the Raspberry PI
# Comment it out the two lines below if you don't use the RasPi
raspi = Runtime.createAndStart("raspi","RasPi")
adaFruit16c.attach("raspi","1","0x40")
#
# This part of the script is if you use the Esp8266_01 service
# Comment it out the two lines below if you don't use the Esp8266_01
# Change COM4 to the port where your Arduino is connected
esp = Runtime.start("esp","Esp8266_01")
adaFruit16c.attach("esp","1","0x40")
#
# This part is common for both devices and creates two servo instances
# on port 3 and 8 on the Adafruit16CServoDriver
# Change the names of the servos and the pin numbers to your usage
thumb = Runtime.start("Thumb", "Servo")
elbow = Runtime.start("Elbow", "Servo")
# attach it to the pwm board - pin 3 & 8
thumb.attach(adaFruit16c,3)
elbow.attach(adaFruit16c,8)
# When this script has been executed you should be able to
# move the servos using the GUI or using python
