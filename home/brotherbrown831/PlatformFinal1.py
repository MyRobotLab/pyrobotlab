from org.myrobotlab.service import Joystick
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Runtime
from time import sleep

#----------------------------------Web Gui--------------------------
webgui = Runtime.create("webgui", "WebGui")
webgui.autoStartBrowser(False)
Runtime.start("webgui", "WebGui")


#---------------------------------Create Services----------------------
arduino = Runtime.createAndStart("arduino","Arduino")
joystick = Runtime.createAndStart("joystick","Joystick")
motorleft = Runtime.start("motorleft","Motor")
motorright = Runtime.start("motorright","Motor")
log = Runtime.start("log","Log")
headturn = Runtime.createAndStart("headturn","Servo")
headtilt = Runtime.createAndStart("headtilt","Servo")


#----------------------Connect Peripherals-----------------------------------
joystick.setController(0); #PC only - Pi needs new
joystick.addInputListener(python)

# Tell the joystick to turn on
joystick.startPolling()

arduino.connect("/dev/ttyACM0");

# attach servos to Arduino
headturn.attach(arduino.getName(), 11)
headtilt.attach(arduino.getName(), 10)
arduino.motorAttach("motorleft", 5, 4) 
arduino.motorAttach("motorright", 6, 7) 

#Detach for safety
headturn.detach()
headtilt.detach()

#------------------------DEFINE STATICVALUES--------------------------
'''
headturn_INIT = 90
headtilt_INIT = 90

headturn_MIN = 10
headtilt_MIN = 30

headturn_MAX = 170
headtilt_MAX = 130
'''

#----------------------Define callback function for Joystick-----------
def onJoystickInput(data):  
  if (data.id == 'A' and float(data.value) == 1.0):
    AttatchAll(1)
  if (data.id == 'B' and float(data.value) == 1.0):
    DetatchAll(1)
  if (data.id == 'ry') and float(data.value == 1.0):
      motorleft.move(1)
      motorright.move(1)
  if (data.id == 'ry') and float(data.value == -1.0):
      motorleft.move(-1)
      motorright.move(-1)
  if (data.id == 'ry') and float(data.value == 0.0):
      motorleft.stop()
      motorright.stop()
  if (data.id == 'rx') and float(data.value == 1.0):
      motorleft.move(-1)
      motorright.move(1)
  if (data.id == 'rx') and float(data.value == -1.0):
      motorleft.move(1)
      motorright.move(-1)
  if (data.id == 'rx') and float(data.value == 0.0):
      motorleft.stop()
      motorright.stop()


#-----------------------------SERVO ACTION----------------------------------------

#----------------------------------Saftey Locks------------------------------------

def AttatchAll(value):
  if (value == 1.0):
    headturn.attach()
    headtilt.attach()
    
def DetatchAll(value):
  if (value == 1.0):
    headturn.detach()
    headtilt.detach()

#-----------------------------------Head Tilt----------------------------
'''
headtilt.setMinMax(40 , 120)
headtilt.moveTo(80)

def StickYListener(value):
  print "Stick Y :" + str(value) + " Current pos: " + str(headtilt.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    headtilt.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  headtilt.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (headtilt.isSweeping()):
      headtilt.setSweeperDelay(delay)
    else:    
      headtilt.sweep(headtilt.pos, headtilt.max, delay, 1, True)
  else:
    if (headtilt.isSweeping()):
      headtilt.setSweeperDelay(delay)
    else:
      headtilt.sweep(headtilt.min, headtilt.pos, delay, -1, True)
'''
