from org.myrobotlab.math import Mapper

mapperPitch = Mapper(-80.0,80.0,-0.8,0.8)
mapperRoll = Mapper(-80.0,40.0,-0.5,0.5)
mapperArm = Mapper(80.0,-80.0,5.0,180.0)

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/ttyUSB0")

i01 = Runtime.start("i01","InMoov")
i01.startHead("/dev/ttyACM0")

i01.startLeftArm("COM5")
leftHand = i01.startLeftHand("COM5")
def closeHand():
  i01.leftHand.setSpeed(0.95,0.95,0.95,0.95,0.95,0.95)
  i01.moveHand("left",61,89,89,104,91,90)

def openHand():
  i01.leftHand.setSpeed(0.95,0.95,0.95,0.95,0.95,0.95)
  i01.moveHand("left",0,0,0,0,0,0)

i01.leftArm.bicep.setMinMax(5,80)

remote = Runtime.start("remote","RemoteAdapter")
myo = Runtime.start("myo","MyoThalmic")
mL = Runtime.start("mL","Motor")
mR = Runtime.start("mR","Motor")
mR.setType2Pwm(6,5)
mL.setType2Pwm(10,11)
mL.attach(arduino);
mR.attach(arduino);

sleep(1)

i01.head.rothead.setInverted(True)
i01.head.neck.setInverted(True)


oculus = Runtime.start("oculus","OculusDIY")

def onOculusData(data):

  i01.head.neck.moveTo(int(data.pitch))
  i01.head.rothead.moveTo(int(data.yaw))

def onMyoData(myodata):
  if (myodata.currentPose == 'DOUBLE_TAP'):
    print "grabbing"
    closeHand()
  elif (myodata.currentPose == 'FIST'):
   print "platform moving forward"
   print mapperPitch.calc(myodata.pitch)
   mL.move(mapperPitch.calc(myodata.pitch))
   mR.move(mapperPitch.calc(myodata.pitch))
  elif (myodata.currentPose == 'FINGERS_SPREAD'):
   print ("moving arm")
   print mapperArm.calc(myodata.pitch)
   i01.leftArm.bicep.moveTo(int(mapperArm.calc(myodata.pitch)))
   if ((mapperArm.calc(myodata.pitch) - 90) >0):
     i01.leftArm.shoulder.moveTo(int(mapperArm.calc(myodata.pitch) - 70))
  elif (myodata.currentPose == 'WAVE_OUT'):
   print "rotating platform"
   print mapperRoll.calc(myodata.roll)
   mL.move(mapperRoll.calc(myodata.roll))
   mR.move((mapperRoll.calc(myodata.roll) * -1.0))
  elif (myodata.currentPose == 'WAVE_IN'):
   print "opening hand"
   openHand()
  else :
   print "stop"
   mL.move(0.0)
   mR.move(0.0)

oculus.addOculusDataListener(python)
myo.addMyoDataListener(python)
remote.startListening()
