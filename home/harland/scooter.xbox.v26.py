# program works on Parallax platform robot and mega board
# uses xbox joystick for control of wheels and inmoov head
# lots of print statements just to let me know what is happening, could be removed
# feb 15 2015 running on mrl 1.0.99
# changed from uno board to mega board to make my life easier
# april 25 2015 pir sensor works to wake up scooter if put to "sleep"

import time
import math
import random

#for desktop software testing
unoPort = "COM6"

i01 = Runtime.createAndStart("i01", "InMoov")

# parallax propeller controller
serial = Runtime.start("serial","Serial")
serial.connect("COM3",115200, 8, 1, 0)

#i01.setMute(True)
# create parts rather than start them so that they may be customized before starting
head = i01.createPeer("head")

# i01.createPeer("head") - but we want a referenced handle on them so we can customize parameters
jaw = head.createPeer("jaw")
eyeX = head.createPeer("eyeX")			#removed servo motor
eyeY = head.createPeer("eyeY")			#removed servo motor
rothead = head.createPeer("rothead")
neck = head.createPeer("neck")
uno = head.createPeer("arduino")
uno.connect(unoPort)

print "pir is working"
readDigitalPin = 4
uno.addListener("publishPin", "python", "input")
uno.setSampleRate(4000)
#i01.startPIR("COM6",4)			#moved to later in code

# used to be custom pins for uno board to be used to control head now using mega bd.
jaw.setPin(26)
eyeX.setPin(22)			#not hooked up yet
eyeY.setPin(24)			#has servo but not connected
rothead.setPin(13)
neck.setPin(12)

# i01.startHead(unoPort, "uno")
i01.startHead(unoPort, "mega")
i01.startMouthControl(unoPort)
i01.startMouth()
#i01.mouth.setLanguage("en")
#i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ella&txt=")
i01.mouth.setLanguage("au")
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Liam&txt=")

i01.head.eyeY.setMinMax(25,85)
i01.head.eyeX.setMinMax(10,60)
i01.head.neck.setMinMax(50,170)
i01.head.rothead.setMinMax(10,170)
i01.head.eyeY.setRest(80)
i01.head.eyeX.setRest(40)
i01.head.neck.setRest(110)
i01.head.rothead.setRest(90)

jaw.setMinMax(50, 110)
i01.head.jaw.map(0,180,110,50)
i01.mouthControl.setmouth(50,110)

print("opencv")
opencv = i01.startOpenCV()
opencv.capture()
#sleep(10) 
#tracker = Runtime.createAndStart("tracker", "Tracking")
#ni = Runtime.createAndStart("ni", "OpenNI")
#ni.startUserTracking()

#3 for microsoft bluetooth joystick
joystickId = 2
#speed for forward motors can be changed with button on xbox
# reverse and turns are fixed at slower speed
speed = 25
serdata = ""
# I/R sensors data not great more like on/off
distcen = 0
distright = 0
distleft = 0
# ping sensors left and right  info very good
distpingright = 0
distpingleft = 0
# battery level
volts = 0
# added so i can limit scotter from waking up to soon as in any movement
timespir = 0

# xbox joystick thanks to kwaters
uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(joystickId)
uberjoy.startPolling()

i01.head.neck.setSpeedControlOnUC(False)
i01.head.rothead.setSpeedControlOnUC(False)
i01.head.eyeY.setSpeedControlOnUC(False)
i01.head.eyeX.setSpeedControlOnUC(False)

def StickRYListener(value):
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep neck up down"
    i01.head.neck.stop()
    return
  absValue = absValue-0.01
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
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep head rotate"
    i01.head.rothead.stop()
    return
  absValue = absValue-0.01
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
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep eye Y"
    i01.head.eyeY.stop()
    return
  absValue = absValue-0.01
  i01.head.eyeY.setSpeed(absValue)
  delay = int((1-absValue) * 200)
  if (value > 0.0):
    if (i01.head.eyeY.isSweeping()):
      i01.head.eyeY.setSweeperDelay(delay)
    else:
      i01.head.eyeY.sweep(i01.head.eyeY.pos, i01.head.eyeY.max, delay, 1, True)
  else:
    if (i01.head.eyeY.isSweeping()):
      i01.head.eyeY.setSweeperDelay(delay)
    else:
      i01.head.eyeY.sweep(i01.head.eyeY.min, i01.head.eyeY.pos, delay, -1, True)

def StickeyeXListener(value):
  absValue = math.fabs(value)
  if (absValue < 0.222):
#    print "Stop sweep eye X"
    i01.head.eyeX.stop()
    return
  absValue = absValue-0.01
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

#set speed value
def ZButtonListener(value):
  global speed
  absValue = math.fabs(value)
#  print "Z raw value = " + str(value)
  if (value > 0.8):
    serial.write("HDLT 20\r")
    speed = speed + 2
    if speed > 70:
      speed = 70
    print "speed= " + str(speed)
    i01.mouth.speak("speed" + str(speed))
    sleep(2)
  if (value < -0.8):
    serial.write("HDLT 00\r")
    speed = 20
#    print "speed= " + str(speed)

# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
# Attach the joystick to the inmoov service servos only activate when the value is 1.0
def AButtonListener(value):
  print("backward")
  if value == 1.0:
    serial.write("HDLT 40\r")			#lights
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(120,88)			#move head in direction of turn
    sleep(.5)
    serial.write("GO D0 D0\r")			#turn move wheels
  if value == 0.0:
    sstop()

def XButtonListener(value):
  print( "go lft")
  if value == 1.0:
    serial.write("HDLT 01\r")
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(90,140)
    sleep(.5)
    serial.write("GO E0 20\r")
  if value == 0.0:
    sstop()
    
def BButtonListener(value):
  print("go rgt")
  if value == 1.0:
    serial.write("HDLT 04\r")
    i01.setHeadSpeed(0.80, 0.80)
    i01.moveHead(90,30)
    sleep(.5)
    serial.write("GO 20 E0\r")
  if value == 0.0:
     sstop()

def fforward():
  global speed
  getping()
  serial.write("HDLT 05\r")
  print("fwd")
  i01.setHeadSpeed(0.80, 0.80)
  i01.moveHead(60,88)
#  irsensors()                            REMOVED 1-12
  if((distpingright >12) and (distpingleft >12)):
      serial.write("GOSPD " + str(speed) + " " + str(speed) + "\r")
  else:
     sstop()

def sstop():
  print("stop")
  serial.write("STOP 0\r")
  serial.write("HDLT 02\r")

def YButtonListener(value):
  global speed
  if value == 1.0:
    fforward()
  if value == 0.0:
    sstop()

def blights(data):
# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
  for i in range (0,data):
     serial.write("HDLT 07\r")
     time.sleep(.5)
     serial.write("HDLT 10\r")
     time.sleep(.5)
     serial.write("HDLT 20\r")
     time.sleep(.5)
  serial.write("HDLT 00\r")
     
def RButtonListener(value):
   if value == 1.0:
      print("rgt-but")
      x = (random.randint(1, 4))
      if x == 1:
        serial.write("HDLT 20\r")
        i01.mouth.speak("i'm looking for a way out of here")
      if x == 2:
        i01.mouth.speak("scooter is lost")
      if x == 3:
        serial.write("HDLT 40\r")
        i01.mouth.speak("scooter is happy")
      if x == 4:
        i01.mouth.speak("i'm hungery")
        blights(2)
      serial.write("HDLT 02\r")
      
def LButtonListener(value):
   if value == 1.0:
      print("lft-but")
 #     i01.mouth.speak("Scooter is taking a break")
      print("at rest")
      i01.powerDown()
      serial.write("HDLT 40\r")
      sleep(60)
      uno.digitalReadPollingStart(readDigitalPin)

def DirPadListener(value):
   if value == 1.0:
      print("auto range mode")
      serial.write("HDLT 10\r")
      i01.mouth.speak("automatic wondering")
#want to spin around scooter and take measurements with ping sensors
#determine FIRST longest distance and move in that direction
#drive there checking ir sensors
#will start out by turning 30 degrees or 12 measurements
      fwddist = 0			#distance to move
      distrgtold = 0			#track last mesasurement
      distlftold = 0
      scootangle = 0			#need to remember where scooter is pointed
      global distpingright
      global distpingleft 
      global distcen
      global distright
      global distleft
      lightpin = 1
      i01.setHeadSpeed(0.70, 0.70)
      i01.moveHead(50,80)                #move head in direction of travel
      for y in range(0,11):		 #do 12 measurements
        serial.write("HDLT " + str(lightpin) + "\r")
#shift bit for next light   each bit runs one light
        lightpin = lightpin << 1
        print("find range position = " + str(y))
        getping()		#get ping distance
# need to save the longest distance and angle
        if (distrgtold < distpingright):
           distrgtold = distpingright
           scootangle = y
        if (distlftold < distpingleft):
           distlftold = distpingleft
           scootangle = y
        print("turn rping=" + str(distpingright) + "in  lping=" + str(distpingleft) + "in " + str(scootangle))
        serial.write("TURN 30 25\r")     #turn 30 deg at a speed of 25
# next line delay needed!        
        sleep(.5)
        
# have distance which is the best now need to turn there
      i01.moveHead(60,50)        #move head in direction of travel
      serial.write("HDLT 07\r")		   #lights in head on
      print( "TURN=" + str(scootangle * 30))
      i01.mouth.speak( "TURN TO " + str(scootangle * 30))
      serial.write("TURN " + str(scootangle * 30) + " 25\r")     #turn to new angle at a speed of 25
      sleep(3)
# move forward longest distance   right or left
      if (distrgtold > distlftold):
         fwddist = distrgtold
      else:
         fwddist = distlftold
      i01.mouth.speak( "distance is " + str(fwddist))
      getping()
      fwddist = fwddist - 12
      print("forward distance = " + str(fwddist) )
# rothead neck eyex eyey jaw
      i01.moveHead(100,70)
      serial.write("ACC 200\r")
      if((distpingright >12) and (distpingleft >12)):				#check for safe distance just incase
# now let move forward but watch the ir sensors
        serial.write("trvl " + str(fwddist) + " 25\r")
        for fdwsteps in range(0,(fwddist / 4)): 
          irsensors()
          if ((distleft > 1000) or (distcen > 1000) or (distright > 1000)):
             print("all stop ir sensor")
             i01.mouth.speak("ir sensor stop")
             break
      sstop()
      blights(2)
      i01.mouth.speak("that was fun")
         
   if value == 0.75:
      print("down arrow, at rest")
      serial.write("HDLT 00\r")
      i01.mouth.speak("scooter at rest")
# head neck 50-170, rotatehead 10-170, eyeX, eyeY 5-60, jaw 50-110
      i01.setHeadSpeed(0.60, 0.60)
      i01.moveHead(60,68)
      batvolts()
      irsensors()
#reset distance counter
      serial.write("RST\r")
      getping()
      i01.mouth.speak( "right ping" + str(distpingright) + "in")
      i01.mouth.speak( "left ping" + str(distpingleft) + "in")
 #     sleep(4)
 #     uno.digitalReadPollingStart(readDigitalPin)
      
   if value == 0.5:
      print("right arrow")
      serial.write("TURN 180 35\r")
      i01.mouth.speak("lets spin")
      blights(1)
      i01.mouth.speak("thats fun")
          
#HEAD
   if value == 0.25:
      print("up arrow, head active")
      serial.write("HDLT 47\r")
      i01.mouth.speak("head")   
      uberjoy.addListener("publishRX", "python", "StickRXheadListener")
      uberjoy.addListener("publishRY", "python", "StickRYheadListener")

def clearbuffer():
  crap = 0
  crap = serial.available()
  print("cbuf " + str(crap))
#would like to clean out serial buffer
  for i in range(1,crap): 
    junk = serial.read()
#    print("junk=" + str(junk))
    
def getadc():  
  global serdata
  clearbuffer()
#send command to read 8 channel atod on eddie board
#  print("adc cmd")
  serial.write("ADC\r")
  time.sleep(1)
  code = 1
#looking for > which is the start of the ADC data
  for i in range(1,90): 
      if(code == 0x3E):
        break
      code = serial.read()
#      print(str(code))
# now read data from ADC and end when you see cr
  serdata = ""
  for i in range(0,31):
    code = (serial.read() & 0xFF)
    serdata += chr(code)
    if ((code == 0x0D)):
#      print("exit")
      break
#  print("raw data=" + str(serdata))
  
def getping(): 
  global distpingright
  global distpingleft 
  global serdata
  clearbuffer()
  serial.write("PING\r")
# need time delay for ping sensor
  sleep(1)
  code = 1
#looking for < which is the start of the ping data 2 sensors
  for i in range(1,60): 
    code = serial.read()
    if(code == 0x3C):
#       print("found start")
       break
#  print("junk data=" + str(serdata))
#read data from ping sensors and end when you see cr
  serdata = ""
  code=1
  for i in range(0,20):
    code = (serial.read() & 0xFF)
    serdata += chr(code)
    if ((code == 0x0D)):
#      print("exit ping")
      break
#  print("raw data=" + str(serdata))
# ping sensor output from 12 to B54 hex  
  distpingright = (((int((serdata[0]), base=16)) * 256) + ((int((serdata[1]), base=16)) * 16) + (int((serdata[2]), base=16)))
  distpingright = distpingright / 23
  if( distpingright == 0 ):
    print("pr>120")
# set to max so you can move forward with no reading    
    distpingright = 120
#    i01.mouth.speak("out of range for right ping")
  else:
    print("pr=" + str(distpingright))
#    i01.mouth.speak( str(distpingright) + "in")
  distpingleft = (((int((serdata[4]), base=16)) * 256) + ((int((serdata[5]), base=16)) * 16) + (int((serdata[6]), base=16)))
  distpingleft = distpingleft / 23
  if( distpingleft == 0 ):
    print("pl>120")
    distpingleft = 120
#    i01.mouth.speak("out of range for left ping")
  else:
    print("pl=" + str(round(distpingleft,1)))
#    i01.mouth.speak( str(distpingleft) + "in")

def batvolts():
#get right values from character stream
#the calculation figures out to be .0039volt per count or 1/.0039=256.4 (was using 238.2)
#using that number shows a voltage that is lower than I see on a voltmeter
#so I adjusted the divisor to match my meter and then round it to 1 places
  global serdata
  global volts
  getadc()
  volts1 = (int((serdata[28]), base=16)) * 256
  volts = (int((serdata[29]), base=16)) * 16
  volts = (volts1 + volts + (int((serdata[30]), base=16))) / 256.4
  volts = volts + 0.65		#adjust for some offset needed
  print(str(round(volts,1)) + "VDC")
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
  getadc()
  distleft = (((int((serdata[8]), base=16)) * 256) + ((int((serdata[9]), base=16)) * 16) + (int(serdata[10], base=16)))
  distcen = (((int((serdata[4]), base=16)) * 256) + ((int((serdata[5]), base=16)) * 16) + (int(serdata[6], base=16)))
  distright = (((int((serdata[0]), base=16)) * 256) + ((int((serdata[0]), base=16)) * 16) + (int(serdata[2], base=16)))
  print("L=" + str(distleft) + " C=" + str(distcen) + " R=" + str(distright))

# note parallax pir is active high, small radio shack pir is active low
# scooter has radio shack pir sensor
# azul has parallax sensor
def input(pin):
  global timespir
#  print( pin.pin, pin.value, pin.type, pin.source )   
  if (pin.value == 0):
     timespir = timespir + 1				#added because it was going off too munch
     if (timespir > 5):
       uno.digitalReadPollingStop(readDigitalPin)     #turn off pir sensor
       timespir = 0				#reset counter for pir
       print pin.pin, pin.value, pin.type, pin.source,    
       print("***    some one is here    ***")		#show me in code working
       i01.mouth.speak("howdy partner, i was resting")
       blights(2)
       for pos in range(0,2):			#move head like waking up
         i01.setHeadSpeed(0.80, 0.80)
         i01.moveHead(100,60)
         sleep(2)
         i01.moveHead(60,110)
         sleep(2)
       i01.moveHead(90,90)
       serial.write("HDLT 05\r")		#lights
 
# invert controls
# dont know how invert works tried but nothing seemed to change
#uberjoy.map("y", -1, 1, 1, -1)
#uberjoy.map("ry", -1, 1, 1, -1)

#startup scooter and reset distance sensor, get battery voltage
batvolts()
irsensors()
serial.write("RST\r")		#reset wheel counters
getping()

# lights in head 01=left face, 02=head-nose, 04=right face
# 08=right eye, 10=kinect, 20=base, 40=red vertical, 00=all off
#blink lights to let me know system is ready
blights(2)
#now start up pir sensor
i01.startPIR("COM6",4)

#uberjoy.addListener("publishX", "python", "StickeyeXListener")
#uberjoy.addListener("publishY", "python", "StickeyeYListener")
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
