#########################################################
# Fred11 motor Cortex Startup Script
#########################################################
# We will be using the following services:
#    Runtime Service
#    RasPi Service
#    Adafruit16CServoDriver
#########################################################
# This script is to  start each of the servo controllers used in the InMoov Robot Fred.
# This is for the top most Raspberry Pi 3 located in Fred's head 
# has an I2C servo interface card installed, this is daisy chained to 3 other
# I2C servo interface controllers, one located on his back and one in each biceps.
    
# This is all running off a Raspberry Pi 3 so we will need to create the RaspPi service. 
# Like all service this is started with a command to the Runtime Service
raspi = Runtime.createAndStart("raspi","RasPi")

# Our servo controllers are the Adafruit 16 channel PWM Servo drivers
# With four of these installed we will need to create four separate service, one for each
# Again we will use the Runtime service to create these Services.
head = Runtime.createAndStart("head", "Adafruit16CServoDriver")
rightArm = Runtime.createAndStart("rightArm", "Adafruit16CServoDriver")
leftArm = Runtime.createAndStart("leftArm", "Adafruit16CServoDriver")
back = Runtime.createAndStart("back", "Adafruit16CServoDriver")

# Next we need to attach the servo drivers to the Raspberry Pi 3.
# There are three parameters we need to set,
# The first is the service we want to attach it to, normally either the RasPi or the Arduino
# in our case it will be the RaspPi
# The second parameter is the bus, This is normally 1 for the RasPi or 0 for the Arduino
# each servo driver has a unique address that is hard coded by means of a set of jumpers 
# on the controller boards, This is our Third parameter, There are seven jumpers that form
# a binary number that is added to 0x40. Note the 0x indicates the number is in hexadecimal format
# that is base 16 and has a range of 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
# 0x40 is equal to 64 in decimal, the seven jumper will give up to 128 possible address
# Just be aware of any other I2C devices you have on the bus and what their address are, 
# some device can not be changed or have a very limited number of selectable addresses.
head.attach("raspi","1","0x40")
rightArm.attach("raspi","1","0x41")
leftArm.attach("raspi","1","0x42")
back.attach("raspi","1","0x43")

# Now that we have the controllers setup we can create the servo.
# This will be done in other script files.
