import time
import math

############################
# Start the InMoov Service
############################
leftPort = "COM15"
rightPort = "COM19"
i01 = Runtime.createAndStart("i01", "InMoov")

# tell the inmoov to be a quiet and obiedient slave.
i01.setMute(True)
i01.startAll(leftPort, rightPort)

############################
# Start the Joystick service
############################
joystickId = 2
uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(joystickId)
uberjoy.startPolling()


# Configure the servos to handle sweeping 
# with a thread in my robot lab and not on the arduinio
i01.rightArm.shoulder.setSpeedControlOnUC(False)
i01.rightArm.rotate.setSpeedControlOnUC(False)
i01.leftArm.shoulder.setSpeedControlOnUC(False)
i01.leftArm.rotate.setSpeedControlOnUC(False)


  
def StickYListener(value):
  print "Stick Y :" + str(value) + " Current pos: " + str(i01.rightArm.shoulder.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    i01.rightArm.shoulder.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  i01.rightArm.shoulder.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.shoulder.isSweeping()):
      i01.rightArm.shoulder.setSweeperDelay(delay)
    else:    
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.pos, i01.rightArm.shoulder.max, delay, 1, True)
  else:
    if (i01.rightArm.shoulder.isSweeping()):
      i01.rightArm.shoulder.setSweeperDelay(delay)
    else:
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.min, i01.rightArm.shoulder.pos, delay, -1, True)

def StickXListener(value):
  print "Stick X :" + str(value) + " Current pos: " + str(i01.rightArm.rotate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    i01.rightArm.rotate.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  i01.rightArm.rotate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.rotate.isSweeping()):
      i01.rightArm.rotate.setSweeperDelay(delay)
    else:    
      i01.rightArm.rotate.sweep(i01.rightArm.rotate.pos, i01.rightArm.rotate.max, delay, 1, True)
  else:
    if (i01.rightArm.rotate.isSweeping()):
      i01.rightArm.rotate.setSweeperDelay(delay)
    else:
      i01.rightArm.rotate.sweep(i01.rightArm.rotate.min, i01.rightArm.rotate.pos, delay, -1, True)


def StickRYListener(value):
  print "Stick RY :" + str(value) + " Current pos: " + str(i01.leftArm.shoulder.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    i01.leftArm.shoulder.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  i01.leftArm.shoulder.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.shoulder.isSweeping()):
      i01.leftArm.shoulder.setSweeperDelay(delay)
    else:    
      i01.leftArm.shoulder.sweep(i01.leftArm.shoulder.pos, i01.leftArm.shoulder.max, delay, 1, True)
  else:
    if (i01.leftArm.shoulder.isSweeping()):
      i01.leftArm.shoulder.setSweeperDelay(delay)
    else:
      i01.leftArm.shoulder.sweep(i01.leftArm.shoulder.min, i01.leftArm.shoulder.pos, delay, -1, True)

def StickRXListener(value):
  print "Stick RX :" + str(value) + " Current pos: " + str(i01.leftArm.rotate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.175):
    print "Stop sweep"
    i01.leftArm.rotate.stop()
    return
  absValue = absValue-0.01
  print "Set Speed " + str(absValue)
  i01.leftArm.rotate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.rotate.isSweeping()):
      i01.leftArm.rotate.setSweeperDelay(delay)
    else:    
      i01.leftArm.rotate.sweep(i01.leftArm.rotate.pos, i01.leftArm.rotate.max, delay, 1, True)
  else:
    if (i01.leftArm.rotate.isSweeping()):
      i01.leftArm.rotate.setSweeperDelay(delay)
    else:
      i01.leftArm.rotate.sweep(i01.leftArm.rotate.min, i01.leftArm.rotate.pos, delay, -1, True)

### Gesture control
############################
# Attach the joystick to 
# the inmoov service servos
# only activate when the value is 1.0
############################
def AButtonListener(value):
  print "A button pressed"  + str(value)
  if value == 1.0:
    i01.rightHand.close()
   
def XButtonListener(value):
  if value == 1.0:
    i01.rightHand.open()  

def BButtonListener(value):
  if value == 1.0:
    i01.leftHand.close()
   
def YButtonListener(value):
  if value == 1.0:
    i01.leftHand.open()

########################################################
# Left Arm Control  (left joystick for rotate and shoulder)
########################################################
# invert control for the y axis
uberjoy.map("y", -1, 1, 1, -1)
uberjoy.map("ry", -1, 1, 1, -1)

uberjoy.addListener("publishX", "python", "StickXListener")
uberjoy.addListener("publishY", "python", "StickYListener")

uberjoy.addListener("publishRX", "python", "StickRXListener")
uberjoy.addListener("publishRY", "python", "StickRYListener")

uberjoy.addListener("publish0", "python", "AButtonListener")
uberjoy.addListener("publish1", "python", "BButtonListener")
uberjoy.addListener("publish2", "python", "XButtonListener")
uberjoy.addListener("publish3", "python", "YButtonListener")

# TODO: figure how to control both biceps ..
# the z button (trigger)is a bit tricky
uberjoy.map("z", 0, 1, i01.rightArm.bicep.max, i01.rightArm.bicep.min)
uberjoy.addZListener(i01.rightArm.bicep)


