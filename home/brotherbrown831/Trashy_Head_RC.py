#script to connect turn and twist motion of head servos to joystick movement
#instead of servo motion being tied directly to servo position the servos will hold thier last position when
#control sticks return to center. Thanks to Kwatters for the syntax on the servo sweeping
#Nolan B. 1/4/16


from org.myrobotlab.service import Joystick
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Runtime
from org.myrobotlab.service import Servo
from time import sleep
#---------------------------------Create Services----------------------
arduino = Runtime.createAndStart("arduino","Arduino")
joystick = Runtime.createAndStart("joystick","Joystick")
servo01 = Runtime.start("servo01","Servo") #Head Tilt Servo
servo02 = Runtime.start("servo02","Servo") #Head Pan Servo

#------------------------Create Static Values-------------------------------
servo01Pin = 10 
servo02Pin = 11 
comPort = "/dev/ttyACM0"
servo01.setMinMax(30, 130)
servo02.setMinMax(30, 130)

#----------------------Connect Peripherals-----------------------------------
joystick.setController(0); #PC only - Pi needs new
joystick.addInputListener(python)
# Tell the joystick to turn on
joystick.startPolling()
#connect Arduino
arduino.connect(comport);
# attach servo
servo01.attach(arduino.getName(), servo01Pin)
servo02.attach(arduino.getName(), servo02Pin)


#----------------------Define callback function for Joystick-----------
def onJoystickInput(data):
  global float(ryValue)
  if (data.id == 'A' and float(data.value) == 1.0):
    print "Attatch Servos"
	AttatchAll(1)
  if (data.id == 'B' and float(data.value) == 1.0):
    print "Detach Servos"
	DetatchAll(1)
  if (data.id == 'y'):
    yValue = float(data.value) 
    printyValue(yValue)
    StickYListener(yValue)
  if (data.id == 'x'):
    xValue = float(data.value) 
    printxValue(xValue)
    StickXListener(xValue)
  
#-----------------------Main Loop----------------------------------------
def printyValue(yValue):
  # this number could easily be used in other speed control functions
  print "the value of y is" + str(yValue)
  
def printxValue(xValue):
  # this number could easily be used in other speed control functions
  print "the value of x is" + str(xValue)
  
def AttatchAll(value):
  if (value == 1.0):
    servo01.attach()
    Servo02.attach()
    
def DetatchAll(value):
  if (value == 1.0):
    servo01.detach()
    Servo02.detach()

#Head Tilt Listener		
def StickYListener(value):
  print "Stick Y :" + str(value) + " Current pos: " + str(servo01.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    servo01.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  servo01.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (servo01.isSweeping()):
      servo01.setSweeperDelay(delay)
    else:    
      servo01.sweep(servo01.pos, servo01.max, delay, 1, True)
  else:
    if (servo01.isSweeping()):
      servo01.setSweeperDelay(delay)
    else:
      servo01.sweep(servo01.min, servo01.pos, delay, -1, True)
	  
#Head Pan Listener
def StickXListener(value):
  print "Stick X :" + str(value) + " Current pos: " + str(servo02.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    servo02.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  servo02.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (servo02.isSweeping()):
      servo02.setSweeperDelay(delay)
    else:    
      servo02.sweep(servo02.pos, servo02.max, delay, 1, True)
  else:
    if (servo02.isSweeping()):
      servo02.setSweeperDelay(delay)
    else:
      servo02.sweep(servo02.min, servo02.pos, delay, -1, True)
