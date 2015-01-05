# program for Azul with control using XBox Joystick with help from Kevin Waters
# same program works on scooter robot  --  lights are only on scooter
# Dec 30 2014

import time
import math

#azul
#leftPort = "COM9"
#rightPort = "COM8"
#scooter
leftPort = "COM9"
rightPort = "COM5"

i01 = Runtime.createAndStart("i01", "InMoov")

serial = Runtime.start("serial","Serial")
#azul
#serial.connect("COM10",115200, 8, 1, 0)
#scooter
serial.connect("COM4",115200, 8, 1, 0)

i01.setMute(True)
i01.startAll(leftPort, rightPort)

#2 for eddie  3 for azul
joystickId = 2
#speed for forward motors, reverse and turn are fixed at slower speed
speed = 15
serdata = ""
# I/R sensors data  turns out this data is not very good
distcen = 0
distright = 0
distleft = 0
# ping sensors left and right  info very good
distpingright = 0
distpingleft = 0

uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(joystickId)
uberjoy.startPolling()

# Configure the servos to handle sweeping with a thread in my robot lab
i01.rightArm.shoulder.setSpeedControlOnUC(False)
i01.rightArm.rotate.setSpeedControlOnUC(False)
i01.rightArm.bicep.setSpeedControlOnUC(False)
i01.rightArm.omoplate.setSpeedControlOnUC(False)

i01.leftArm.shoulder.setSpeedControlOnUC(False)
i01.leftArm.rotate.setSpeedControlOnUC(False)
i01.leftArm.bicep.setSpeedControlOnUC(False)
i01.leftArm.omoplate.setSpeedControlOnUC(False)

i01.head.neck.setSpeedControlOnUC(False)
i01.head.rothead.setSpeedControlOnUC(False)

def StickYListener(value):
#  print "Stick Y :" + str(value) + " Current pos: " + str(i01.rightArm.shoulder.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep right shoulder"
    i01.rightArm.shoulder.stop()
    return
  absValue = absValue-0.01
  print "right arm SpeedY " + str(absValue)
  i01.rightArm.shoulder.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.shoulder.isSweeping()):
      i01.rightArm.shoulder.setSweeperDelay(delay)
    else:
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.pos, i01.rightArm.shoulder.max,delay, 1, True)
  else:
    if (i01.rightArm.shoulder.isSweeping()):
      i01.rightArm.shoulder.setSweeperDelay(delay)
    else:
      i01.rightArm.shoulder.sweep(i01.rightArm.shoulder.min, i01.rightArm.shoulder.pos,delay, -1, True)

def StickYlfListener(value):
#  print "Stick Y :" + str(value) + " Current pos: " + str(i01.leftArm.shoulder.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep left shoulder"
    i01.leftArm.shoulder.stop()
    return
  absValue = absValue-0.01
  print "left arm SpeedYLF " + str(absValue)
  i01.leftArm.shoulder.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.shoulder.isSweeping()):
      i01.leftArm.shoulder.setSweeperDelay(delay)
    else:
      i01.leftArm.shoulder.sweep(i01.leftArm.shoulder.pos, i01.leftArm.shoulder.max,delay, 1, True)
  else:
    if (i01.leftArm.shoulder.isSweeping()):
      i01.leftArm.shoulder.setSweeperDelay(delay)
    else:
      i01.leftArm.shoulder.sweep(i01.leftArm.shoulder.min, i01.leftArm.shoulder.pos,delay, -1, True)

def StickXListener(value):
#  print "Stick X :" + str(value) + " Current pos: " + str(i01.rightArm.rotate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep right rotate"
    i01.rightArm.rotate.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedX " + str(absValue)
  i01.rightArm.rotate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.rotate.isSweeping()):
      i01.rightArm.rotate.setSweeperDelay(delay)
    else:
      i01.rightArm.rotate.sweep(i01.rightArm.rotate.pos, i01.rightArm.rotate.max, delay, 1,True)
  else:
    if (i01.rightArm.rotate.isSweeping()):
      i01.rightArm.rotate.setSweeperDelay(delay)
    else:
      i01.rightArm.rotate.sweep(i01.rightArm.rotate.min, i01.rightArm.rotate.pos, delay, -1,True)
      
def StickXlfListener(value):
#  print "Stick X :" + str(value) + " Current pos: " + str(i01.leftArm.rotate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep left rotate"
    i01.leftArm.rotate.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedXLF " + str(absValue)
  i01.leftArm.rotate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.rotate.isSweeping()):
      i01.leftArm.rotate.setSweeperDelay(delay)
    else:
      i01.leftArm.rotate.sweep(i01.leftArm.rotate.pos, i01.leftArm.rotate.max, delay, 1,True)
  else:
    if (i01.leftArm.rotate.isSweeping()):
      i01.leftArm.rotate.setSweeperDelay(delay)
    else:
      i01.leftArm.rotate.sweep(i01.leftArm.rotate.min, i01.leftArm.rotate.pos, delay, -1,True)

def StickRYListener(value):
#  print "Stick RY :" + str(value) + " Current pos: " + str(i01.rightArm.bicep.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep right bicep"
    i01.rightArm.bicep.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRY " + str(absValue)
  i01.rightArm.bicep.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.bicep.isSweeping()):
      i01.rightArm.bicep.setSweeperDelay(delay)
    else:
      i01.rightArm.bicep.sweep(i01.rightArm.bicep.pos, i01.rightArm.bicep.max, delay, 1,True)
  else:
    if (i01.rightArm.bicep.isSweeping()):
      i01.rightArm.bicep.setSweeperDelay(delay)
    else:
      i01.rightArm.bicep.sweep(i01.rightArm.bicep.min, i01.rightArm.bicep.pos, delay, -1,True)

def StickRYlfListener(value):
#  print "Stick RY :" + str(value) + " Current pos: " + str(i01.leftArm.bicep.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep left bicep"
    i01.leftArm.bicep.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRY " + str(absValue)
  i01.leftArm.bicep.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.bicep.isSweeping()):
      i01.leftArm.bicep.setSweeperDelay(delay)
    else:
      i01.leftArm.bicep.sweep(i01.leftArm.bicep.pos, i01.leftArm.bicep.max, delay, 1,True)
  else:
    if (i01.leftArm.bicep.isSweeping()):
      i01.leftArm.bicep.setSweeperDelay(delay)
    else:
      i01.leftArm.bicep.sweep(i01.leftArm.bicep.min, i01.leftArm.bicep.pos, delay, -1,True)

def StickRXListener(value):
#  print "Stick RX :" + str(value) + " Current pos: " + str(i01.rightArm.omoplate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep right omoplate"
    i01.rightArm.omoplate.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRX " + str(absValue)
  i01.rightArm.omoplate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.rightArm.omoplate.isSweeping()):
      i01.rightArm.omoplate.setSweeperDelay(delay)
    else:
      i01.rightArm.omoplate.sweep(i01.rightArm.omoplate.pos, i01.rightArm.omoplate.max,delay, 1, True)
  else:
    if (i01.rightArm.omoplate.isSweeping()):
      i01.rightArm.omoplate.setSweeperDelay(delay)
    else:
      i01.rightArm.omoplate.sweep(i01.rightArm.omoplate.min, i01.rightArm.omoplate.pos,delay, -1, True)

def StickRXlfListener(value):
#  print "Stick RX :" + str(value) + " Current pos: " + str(i01.leftArm.omoplate.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep left omoplate"
    i01.leftArm.omoplate.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRXLF " + str(absValue)
  i01.leftArm.omoplate.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.leftArm.omoplate.isSweeping()):
      i01.leftArm.omoplate.setSweeperDelay(delay)
    else:
      i01.leftArm.omoplate.sweep(i01.leftArm.omoplate.pos, i01.leftArm.omoplate.max,delay, 1, True)
  else:
    if (i01.leftArm.omoplate.isSweeping()):
      i01.leftArm.omoplate.setSweeperDelay(delay)
    else:
      i01.leftArm.omoplate.sweep(i01.leftArm.omoplate.min, i01.leftArm.omoplate.pos,delay, -1, True)

def StickRYheadListener(value):
#  print "Stick RY neck up-down :" + str(value) + " Current pos: " + str(i01.head.neck.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep neck up down"
    i01.head.neck.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRY " + str(absValue)
  i01.head.neck.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.head.neck.isSweeping()):
      i01.head.neck.setSweeperDelay(delay)
    else:
      i01.head.neck.sweep(i01.head.neck.pos, i01.head.neck.max, delay, 1, True)
  else:
    if (i01.head.neck.isSweeping()):
      i01.head.neck.setSweeperDelay(delay)
    else:
      i01.head.neck.sweep(i01.head.neck.min, i01.head.neck.pos, delay, -1, True)

def StickRXheadListener(value):
#  print "Stick RX head rotate :" + str(value) + " Current pos: " + str(i01.head.rothead.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep head rotate"
    i01.head.rothead.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedRX " + str(absValue)
  i01.head.rothead.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.head.rothead.isSweeping()):
      i01.head.rothead.setSweeperDelay(delay)
    else:
      i01.head.rothead.sweep(i01.head.rothead.pos, i01.head.rothead.max, delay, 1, True)
  else:
    if (i01.head.rothead.isSweeping()):
      i01.head.rothead.setSweeperDelay(delay)
    else:
      i01.head.rothead.sweep(i01.head.rothead.min, i01.head.rothead.pos, delay, -1, True)

def ZButtonListener(value):
  global speed
  absValue = math.fabs(value)
  print "Z raw value = " + str(value)
  if (value > 0.8):
    print("lights on, z pos")
    serial.write("HDLT FF\r")
    speed = speed + 2
    if speed > 70:
      speed = 70
    print "speed= " + str(speed)
    i01.mouth.speak("speed" + str(speed))
    time.sleep(5)
  if (value < -0.8):
    print("lights off, z neg")
    serial.write("HDLT 00\r")
    speed = 20
    print "speed= " + str(speed)
    
# Attach the joystick to the inmoov service servos only activate when the value is 1.0
def AButtonListener(value):
  print("BACKWARD")
  if value == 1.0:
    serial.write("HDLT 40\r")
    serial.write("GO D0 D0\r")
#     time.sleep(1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")

def XButtonListener(value):
  if value == 1.0:
    print( "left turn")
    serial.write("HDLT 01\r")
    serial.write("GO A0 40\r")
#    time.sleep(1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")
    
def BButtonListener(value):
  if value == 1.0:
    print("right turn")
    serial.write("HDLT 02\r")
    serial.write("GO 40 A0\r")
#    time.sleep(1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")

def YButtonListener(value):
  global speed
  if value == 1.0:
    getping()
    serial.write("HDLT 03\r")
    print("forward")
    serial.write("GO 15 15\r")
    if((distpingright >12) and (distpingleft >12)):
#      serial.write("GO 15 15\r")
      serial.write("GO " + str(speed) + " " + str(speed) + "\r")
    if value == 0.0:
      serial.write("STOP 0\r")
      serial.write("HDLT 00\r")
      print("STOP")
      
def RButtonListener(value):
   if value == 1.0:
      print("open hands")
      i01.mouth.speak("open hands")
#      i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
#      i01.setHandSpeed("right", 0.85, 0.85, 0.85, 0.85, 0.85, 0.85)
      i01.moveHand("right",0,0,0,0,0)
      time.sleep(2)
      i01.moveHand("left",0,0,0,0,0)
      
def LButtonListener(value):
   if value == 1.0:
      print("close hands")
      i01.mouth.speak("close hands")
#      i01.setHandSpeed("left", 0.70, 0.70, 0.70, 0.70, 0.70, 0.70)
#      i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 0.70)
      i01.moveHand("right",180,180,180,180,180)
      time.sleep(2)
      i01.moveHand("left",180,180,180,180,180)

def DirPadListener(value):
#LEFT ARM
   if value == 1.0:
      print("left arrow, left arm")
      serial.write("HDLT 01\r")
      i01.mouth.speak("left arm")
#RIGHT OFF
      uberjoy.removeListener("publishX", "python", "StickXListener")
      uberjoy.removeListener("publishY", "python", "StickYListener")
      uberjoy.removeListener("publishRX", "python", "StickRXListener")
      uberjoy.removeListener("publishRY", "python", "StickRYListener")
#HEAD OFF    
      uberjoy.removeListener("publishRX", "python", "StickRXlfListener")
      uberjoy.removeListener("publishRY", "python", "StickRYlfListener")
#LEFT ARM ON      
      uberjoy.addListener("publishRX", "python", "StickRXlfListener")
      uberjoy.addListener("publishRY", "python", "StickRYlfListener")
      uberjoy.addListener("publishX", "python", "StickXlfListener")
      uberjoy.addListener("publishY", "python", "StickYlfListener")
      serial.write("HDLT 00\r")

   if value == 0.75:
      print("down arrow, azul rest")
      serial.write("HDLT 04\r")
      i01.mouth.speak("azuul at rest and motors stop")
# head rotatehead 15-165, neck 10-150, eyeX 20-80, eyeY 20-80, jaw 10-65
      i01.moveHead(90,65,60,60,45)
      time.sleep(.25)
# arm left  bicep 0-90, rotate 0-120, shoulder 0-90,  omoplate 0-65
      i01.moveArm("left",20,90,30,20)
      time.sleep(.25)
# arm right bicep 0-80, rotate 0-160, shoulder 0-180, omoplate 0-75
      i01.moveArm("right",20,90,30,20)
      time.sleep(.25)
# hand left  thumb 30-140, index 25-150, majeure 20-160, ring 20-140, pinky 0-110, wrist 0-150
      i01.moveHand("left",35,30,25,25,5,90)
      time.sleep(.25)
# hand right thumb 25-110, index 0-100,  majeure 5-140,  ring 0-115,  pinky 0-115, wrist 10-90
      i01.moveHand("right",25,5,15,10,10,70)
#      time.sleep(.25)
      serial.write("STOP 0\r")
# torso topStom 95-140
#      i01.moveTorso(115,90,90)
      getadc()
      batvolts()
      irsensors()
      #reset distance counter
      serial.write("RST\r")
      getping()
      i01.mouth.speak( str(round(distpingright,1)) + "inches")
      i01.mouth.speak( str(round(distpingleft,1)) + "inches")

#RIGHT ARM
   if value == 0.5:
      print("right arrow, right arm")
      serial.write("HDLT 01\r")
      i01.mouth.speak("right arm")
#HEAD OFF
      uberjoy.removeListener("publishRX", "python", "StickRXheadListener")
      uberjoy.removeListener("publishRY", "python", "StickRYheadListener")
#LEFT ARM OFF      
      uberjoy.removeListener("publishRX", "python", "StickRXlfListener")
      uberjoy.removeListener("publishRY", "python", "StickRYlfListener")
      uberjoy.removeListener("publishX", "python", "StickXlfListener")
      uberjoy.removeListener("publishY", "python", "StickYlfListener")
#RIGHT ARM ON      
      uberjoy.addListener("publishX", "python", "StickXListener")
      uberjoy.addListener("publishY", "python", "StickYListener")
      uberjoy.addListener("publishRX", "python", "StickRXListener")
      uberjoy.addListener("publishRY", "python", "StickRYListener")

#HEAD
   if value == 0.25:
      print("up arrow, head active")
      serial.write("HDLT F0\r")
      i01.mouth.speak("head")
#RIGHT ARM OFF
      uberjoy.removeListener("publishRX", "python", "StickRXListener")
      uberjoy.removeListener("publishRY", "python", "StickRYListener")
#HEAD ON     
      uberjoy.addListener("publishRX", "python", "StickRXheadListener")
      uberjoy.addListener("publishRY", "python", "StickRYheadListener")

def getadc():  
#send command to read 8 channel atod on eddie board
  serial.write("ADC\r")
  time.sleep(1)
  code = 1
  global serdata
#next 7 lines because serial command can come back with empty character which causes code to crash
  for i in range(1,5): 
    try:
      code = serial.read()
      serdata += chr(code)
    except:
        print("oops. this is crap!")
        pass
#remove any junk in input buffer on serial port
#looking for > which is the start of the ADC data
#every command to the eddie bd gets some kind of characters sent back
  for i in range(1,60): 
      code = serial.read()
#  print("junk=" + chr(code) + " " + str(code))
      if(code == 0x3E):
#        print("found end")
        break
      serdata += chr(code)
#  print("junk data=" + str(serdata))
# now read data from ADC and end when you see cr
  serdata = ""
  code=1
  for i in range(0,31):
    code = (serial.read() & 0xFF)
    serdata += chr(code)
    if ((code == 0x0D)):
      print("exit")
      break
#  print("raw data=" + str(serdata))
  
def getping(): 
  global distpingright
  global distpingleft 
  serial.write("PING\r")
# need time delay for ping sensor
  time.sleep(1)
  code = 1
#looking for < which is the start of the ping data 2 sensors
  global serdata
  for i in range(1,60): 
    code = serial.read()
    if(code == 0x3C):
#       print("found end")
       break
    serdata += chr(code)
#  print("junk data=" + str(serdata))
#read data from ping sensors and end when you see cr
  serdata = ""
  code=1
  for i in range(0,20):
    code = (serial.read() & 0xFF)
    serdata += chr(code)
    if ((code == 0x0D)):
#      print("exit")
      break
#  print("raw data=" + str(serdata))
# ping sensor output from 12 to B54 hex  
  distpingright = (((int((serdata[0]), base=16)) * 256) + ((int((serdata[1]), base=16)) * 16) + (int((serdata[2]), base=16)))
  distpingright = distpingright / 23
  if( distpingright == 0 ):
    print("out of range")
#    i01.mouth.speak("out of range for right ping sensor")
  else:
    print("ping right =" + str(round(distpingright,1)) + " in")
#    i01.mouth.speak( str(round(distpingright,1)) + "inches")
  distpingleft = (((int((serdata[4]), base=16)) * 256) + ((int((serdata[5]), base=16)) * 16) + (int((serdata[6]), base=16)))
  distpingleft = distpingleft / 23
  if( distpingleft == 0 ):
    print("out of range")
#    i01.mouth.speak("out of range for left ping sensor")
  else:
    print("ping left =" + str(round(distpingleft,1)) + " in")
#    i01.mouth.speak( str(round(distpingleft,1)) + "inches")

def batvolts():
#get right values from character stream
#the calculation figures out to be .0039volt per count or 1/.0039=256.4
#using that number shows a voltage that is lower than I see on a voltmeter
#so I adjusted the divisor to match my meter and then round it to 1 places
  global serdata
  volts1 = (int((serdata[28]), base=16)) * 256
  volts = (int((serdata[29]), base=16)) * 16
  volts = (volts1 + volts + (int((serdata[30]), base=16))) / 238.2
  print("batt =" + str(round(volts,1)) + "VDC")
  i01.mouth.speak( str(round(volts,1)) + "volts")

def irsensors():
# 3 I/R sensors on platform measure from 10 to 80cm or 3.94 to 31.5inches
# ADC is 12 bit or FFF but eddie bd only uses 10 bits or 1024 counts
# note spec says out voltage at 80cm is .25 to .55v and at 10cm is 1.85 to 2.7v
# so these are more like on off for set distance not very accurate for real distance
# 30cm or 11.8 inches should be good starting point or about 1 volt for center
# may want closer for sides    want to be able to go through doors
# 1 volt should be around 1024 cnts/5v or about 205 counts
# remember higher voltage is closer
  global serdata
  global distcen
  global distright
  global distleft
  distcen = (int((serdata[8]), base=16)) * 256
  distcen1 = (int((serdata[9]), base=16)) * 16
  distleft = (distcen + distcen1 + (int(serdata[10], base=16)))
  print("IR left =" + str(distleft))
  if(distleft > 600):
    print("close left")
  distcen = (int((serdata[4]), base=16)) * 256
  distcen1 = (int((serdata[5]), base=16)) * 16
  distcen = (distcen + distcen1 + (int(serdata[6], base=16)))
  print("IR center =" + str(distcen))
  if(distcen > 600):
    print("close center")
  distcen = (int((serdata[0]), base=16)) * 256
  distcen1 = (int((serdata[1]), base=16)) * 16
  distright = (distcen + distcen1 + (int(serdata[2], base=16)))
  print("IR right =" + str(distright))
  if(distright > 600):
    print("close right")

# Arm Control invert control for the y axis
uberjoy.map("y", -1, 1, 1, -1)
#uberjoy.map("ry", -1, 1, 1, -1)
#startup eddie and reset distance sensor, get battery voltage
getadc()
batvolts()
irsensors()
serial.write("RST\r")
getping()

#blink lights to let me know system is ready
for i in range (1,10):
  serial.write("HDLT FF\r")
  time.sleep(.5)
  serial.write("HDLT 00\r")
  time.sleep(.5)
i01.mouth.speak("azuul is ready")

uberjoy.addListener("publishX", "python", "StickXListener")
uberjoy.addListener("publishY", "python", "StickYListener")
uberjoy.addListener("publishRX", "python", "StickRXListener")
uberjoy.addListener("publishRY", "python", "StickRYListener")
uberjoy.addListener("publish0", "python", "AButtonListener")
uberjoy.addListener("publish1", "python", "BButtonListener")
uberjoy.addListener("publish2", "python", "XButtonListener")
uberjoy.addListener("publish3", "python", "YButtonListener")
uberjoy.addListener("publish4", "python", "LButtonListener")
uberjoy.addListener("publish5", "python", "RButtonListener")
uberjoy.addListener("publishZ", "python", "ZButtonListener")
uberjoy.addListener("publishPOV", "python", "DirPadListener")
