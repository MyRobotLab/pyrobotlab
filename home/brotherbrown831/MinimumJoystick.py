from org.myrobotlab.service import Joystick
from org.myrobotlab.service import Runtime
from time import sleep
#---------------------------------Create Services----------------------
joystick = Runtime.createAndStart("joystick","Joystick")

#----------------------Connect Peripherals-----------------------------------
joystick.setController(0); #PC only - Pi needs new
joystick.addInputListener(python)
# Tell the joystick to turn on
joystick.startPolling()

#----------------------Define callback function for Joystick-----------
def onJoystickInput(data):
  global float(ryValue)
  if (data.id == 'A' and float(data.value) == 1.0):
    print "Attatch MotorLeft"
  if (data.id == 'B' and float(data.value) == 1.0):
    print "Detach MotorLeft"
  if (data.id == 'ry'):
    ryValue = float(data.value) 
  
def print "the value of ry is" (ryValue)# this number could easily be used in other speed control functions
''' 
example use
def motorLeft.move(255*(ryValue):
