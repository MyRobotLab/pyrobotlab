from org.myrobotlab.service import Joystick
from org.myrobotlab.service import Runtime
from time import sleep

#---------------------------------Create Services----------------------
joystick = Runtime.createAndStart("joystick","Joystick")

#----------------------Define callback function for Joystick-----------
def onJoystickInput(data):
  print data
  if (data.id == '0' and float(data.value) == 1.0):
    print "A Button has been pushed"

#----------------------Connect Peripherals-----------------------------------
joystick.setController(2); #PC only - Pi needs new
joystick.addInputListener(python)

# Tell the joystick to turn on 
joystick.startPolling()
