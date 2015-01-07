# program works on Parallax platform robot and UNO board
# uses xbox joystick for control
# lots of print statements just to let me know what is happening, could be removed
# Jan 4 2015

import time
import math
import random

#parallax platform on desktop computer
#unoPort = "COM5"
#parallax platform on scooter laptop
unoPort = "COM11"

i01 = Runtime.createAndStart("i01", "InMoov")

# parallax propeller controller
serial = Runtime.start("serial","Serial")
serial.connect("COM4",115200, 8, 1, 0)

#i01.setMute(True)
# create parts rather than start them so that they may be customized before starting
head = i01.createPeer("head")

# all these services were created with the
# i01.createPeer("head") - but we want a referenced handle on them
# so we can customize parameters
jaw = head.createPeer("jaw")
eyeX = head.createPeer("eyeX")
eyeY = head.createPeer("eyeY")
rothead = head.createPeer("rothead")
neck = head.createPeer("neck")
uno = head.createPeer("arduino")
uno.connect(unoPort)

# custom pins - must be done before
jaw.setPin(6)
eyeX.setPin(3)
eyeY.setPin(2)
rothead.setPin(4)
neck.setPin(5)

i01.startHead(unoPort, "uno")
i01.startMouthControl(unoPort)
i01.startMouth()
#to tweak the default voice
#i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
#i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Will&txt=")
i01.mouth.setLanguage("en") # Google supports some language codes

i01.head.eyeY.setMinMax(5,60)
i01.head.eyeX.setMinMax(10,60)
i01.head.neck.setMinMax(0,180)
i01.head.rothead.setMinMax(10,170)
i01.head.eyeY.setRest(20)
i01.head.eyeX.setRest(40)
i01.head.neck.setRest(90)
i01.head.rothead.setRest(88)

jaw.setMinMax(50, 110)
i01.head.jaw.map(0,180,110,50)
i01.mouthControl.setmouth(50,110)

#2 for usb wired joystick
#3 for microsoft bluetooth joystick
joystickId = 3
#speed for forward motors, reverse and turn are fixed at slower speed
speed = 25
serdata = ""
# I/R sensors data  turns out this data is not very good
distcen = 0
distright = 0
distleft = 0
# ping sensors left and right  info very good
distpingright = 0
distpingleft = 0

# xbox joystick thanks to kwaters
uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(joystickId)
uberjoy.startPolling()

i01.head.neck.setSpeedControlOnUC(False)
i01.head.rothead.setSpeedControlOnUC(False)
i01.head.eyeY.setSpeedControlOnUC(False)
i01.head.eyeX.setSpeedControlOnUC(False)

def StickRYListener(value):
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

def StickRXListener(value):
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

def StickeyeYListener(value):
#  print "Stick eye Y :" + str(value) + " Current pos: " + str(i01.head.neck.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep eye Y"
    i01.head.eyeY.stop()
    return
  absValue = absValue-0.01
  print "Set SpeedeyeY " + str(absValue)
  i01.head.eyeY.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.head.eyeY.isSweeping()):
      i01.head.eyeY.setSweeperDelay(delay)
    else:
      i01.head.eyeY.sweep(i01.eyeY.neck.pos, i01.eyeY.neck.max, delay, 1, True)
  else:
    if (i01.head.eyeY.isSweeping()):
      i01.head.eyeY.setSweeperDelay(delay)
    else:
      i01.head.eyeY.sweep(i01.head.eyeY.min, i01.head.eyeY.pos, delay, -1, True)

def StickeyeXListener(value):
#  print "Stick eye X head rotate :" + str(value) + " Current pos: " + str(i01.head.rothead.pos)
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep eye X"
    i01.head.eyeX.stop()
    return
  absValue = absValue-0.01
  print "Set Speed eye X " + str(absValue)
  i01.head.eyeX.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.head.eyeX.isSweeping()):
      i01.head.eyeX.setSweeperDelay(delay)
    else:
      i01.head.eyeX.sweep(i01.head.eyeX.pos, i01.head.eyeX.max, delay, 1, True)
  else:
    if (i01.head.eyeX.isSweeping()):
      i01.head.eyeX.setSweeperDelay(delay)
    else:
      i01.head.eyeX.sweep(i01.head.eyeX.min, i01.head.eyeX.pos, delay, -1, True)

def ZButtonListener(value):
  global speed
  absValue = math.fabs(value)
  print "Z raw value = " + str(value)
  if (value > 0.8):
    print("lights on, z pos")
    serial.write("HDLT 20\r")
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

# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
# Attach the joystick to the inmoov service servos only activate when the value is 1.0
def AButtonListener(value):
  print("BACKWARD")
  if value == 1.0:
    serial.write("HDLT 40\r")
    serial.write("GO E0 E0\r")
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(60,88,85,40,100)
#     time.sleep(1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")

def XButtonListener(value):
  if value == 1.0:
    print( "left turn")
    serial.write("HDLT 01\r")
    serial.write("GO E0 10\r")
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(60,160,85,40,90)
#    time.sleep(.1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")
    
def BButtonListener(value):
  if value == 1.0:
    print("right turn")
    serial.write("HDLT 04\r")
    serial.write("GO 10 E0\r")
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(60,20,85,40,70)
#    time.sleep(.1)
  if value == 0.0:
    serial.write("STOP 0\r")
    serial.write("HDLT 00\r")

def fforward():
  global speed
  getping()
  serial.write("HDLT 07\r")
  print("forward")
  i01.setHeadSpeed(0.80, 0.80)
  i01.moveHead(60,88,85,40,100)
#  time.sleep(.1)
  if((distpingright >12) and (distpingleft >12)):
      serial.write("GO " + str(speed) + " " + str(speed + 2) + "\r")
  else:
     sstop()

def sstop():
# print("stop motors")
  serial.write("STOP 0\r")
  serial.write("HDLT 05\r")
  print("STOP")

def YButtonListener(value):
  global speed
  if value == 1.0:
    fforward()
  if value == 0.0:
    sstop()

def blights():
# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
  for i in range (1,10):
     serial.write("HDLT 05\r")
     sleep(.1)
     serial.write("HDLT 10\r")
     sleep(.1)
     serial.write("HDLT 20\r")
     sleep(.1)
     serial.write("HDLT 40\r")
     sleep(.1)
     serial.write("HDLT 07\r")
     sleep(.1)
     serial.write("HDLT 00\r")
     sleep(.1)
     
def RButtonListener(value):
   if value == 1.0:
      print("right button")
      i01.mouth.speak("scooter thanks kevin for the joystick routine")
      time.sleep(1)
      i01.mouth.speak("and thanks grog for the pin define commands")
      blights()
      
def LButtonListener(value):
   if value == 1.0:
      print("left button")
      i01.mouth.speak("Hello, my name is Scooter, Azuls shorter cousin and the black sheep of the family")
      blights()

def DirPadListener(value):
#LEFT ARM
   if value == 1.0:
      print("left arrow")
      serial.write("HDLT 20\r")
      i01.mouth.speak("automatic wondering")
#determines how many gestures are done      
      for y in range(0,10):
        x = (random.randint(1,6))
        print("gesture number = " + str(y))
        if x == 1:
           print("1 FORWARD")
           fforward()
           time.sleep(3)
           sstop()
        if x == 2:
           print("2 lights")
           blights()
           sleep(1)
           blights()
           sleep(1)
        if x == 3:
           print("3 speak")
           i01.mouth.speak("hey Azul let's do something")
           sleep(1)
        if x == 4:
           print("4 turn")
           serial.write("HDLT 01\r")
           serial.write("TURN 45 20\r")
           i01.setHeadSpeed(0.80, 0.80)
           i01.moveHead(60,160,85,40,90)
           serial.write("HDLT 01\r")
           serial.write("TURN 45 20\r")
           time.sleep(3)
           serial.write("STOP 0\r")
           serial.write("HDLT 00\r")
        if x == 5:
           print("5 BACKWARD")
           serial.write("HDLT 40\r")
           serial.write("GO E0 E5\r")
           i01.setHeadSpeed(0.80, 0.80)
           i01.moveHead(60,88,85,40,100)
           time.sleep(3)
           serial.write("STOP 0\r")
           serial.write("HDLT 00\r")       
        if x == 6:
# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
          print("6 just head lights")
          for i in range (1,5):
            serial.write("HDLT 01\r")
            sleep(.3)
            serial.write("HDLT 02\r")
            sleep(.3)
            serial.write("HDLT 04\r")
            sleep(.3)
            serial.write("HDLT 08\r")
            sleep(.3)
            serial.write("HDLT 07\r")
            sleep(.3)
            serial.write("HDLT 00\r")
            sleep(.3)
          
   if value == 0.75:
      print("down arrow, scooter at rest")
      serial.write("HDLT 00\r")
      i01.mouth.speak("scooter at rest and motors stop")
# head neck, rotatehead 10-170, eyeX, eyeY 5-60, jaw 50-110
      i01.setHeadSpeed(1.00, 1.00)
      i01.moveHead(60,88,60,60,45)
      time.sleep(.2)
      getadc()
      batvolts()
      irsensors()
      #reset distance counter
      serial.write("RST\r")
      getping()
      i01.mouth.speak( "right ping" + str(round(distpingright,1)) + "inches")
      i01.mouth.speak( "left ping" + str(round(distpingleft,1)) + "inches")

   if value == 0.5:
      print("right arrow")
      serial.write("HDLT 20\r")
      i01.mouth.speak("right arrow direction pad")
      blights()
      serial.write("TURN 180 35\r")
           

#HEAD
   if value == 0.25:
      print("up arrow, head active")
      serial.write("HDLT 47\r")
      i01.mouth.speak("head")   
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
      if(code == 0x3E):
        print("found end 1st time")
        break
    except:
        print("oops. this is crap!")
        pass
#remove any junk in input buffer on serial port
#looking for > which is the start of the ADC data
#every command to the eddie bd gets some kind of characters sent back
  for i in range(1,90): 
      if(code == 0x3E):
        print("found end 2nd time")
        break
      code = serial.read()
#  print("junk=" + chr(code) + " " + str(code))
      if(code == 0x3E):
        print("found end the last time")
        break
      serdata += chr(code)
  print("junk data=" + str(serdata))
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
# set to max so you can move forward with no reading    
    distpingright = 120
#    i01.mouth.speak("out of range for right ping sensor")
  else:
    print("ping right =" + str(round(distpingright,1)) + " in")
#    i01.mouth.speak( str(round(distpingright,1)) + "inches")
  distpingleft = (((int((serdata[4]), base=16)) * 256) + ((int((serdata[5]), base=16)) * 16) + (int((serdata[6]), base=16)))
  distpingleft = distpingleft / 23
  if( distpingleft == 0 ):
    print("out of range")
    distpingleft = 120
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
# remember higher number is closer
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

# invert control for the y axis
uberjoy.map("y", -1, 1, 1, -1)
#uberjoy.map("ry", -1, 1, 1, -1)

#startup scooter and reset distance sensor, get battery voltage
getadc()
batvolts()
irsensors()
serial.write("RST\r")
getping()

# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
#blink lights to let me know system is ready
blights()
i01.mouth.speak("scooter is ready")

uberjoy.addListener("publishX", "python", "StickeyeXListener")
uberjoy.addListener("publishY", "python", "StickeyeYListener")
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
