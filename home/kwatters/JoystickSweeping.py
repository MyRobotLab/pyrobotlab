i01.rightArm.shoulder.setSpeedControlOnUC(False)
  
def StickXListener(value):
  print "Stick X :" + str(value) + " Current pos: " + str(i01.rightArm.shoulder.pos)
  
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
      i01.rightArm.shoulder.setDelay(delay)
    else:    
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.pos, i01.rightArm.shoulder.max, delay, 1, True)
  else:
    if (i01.rightArm.shoulder.isSweeping()):
      i01.rightArm.shoulder.setDelay(delay)
    else:
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.min, i01.rightArm.shoulder.pos, delay, -1, True)
    
########################################################
# Left Arm Control  (left joystick for rotate and shoulder)
########################################################
uberjoy.map("x", -1, 1, -1, 1)
uberjoy.addListener("publishX", "python", "StickXListener")