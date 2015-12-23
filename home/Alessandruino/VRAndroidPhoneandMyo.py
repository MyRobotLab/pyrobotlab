from org.myrobotlab.math import Mapper

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/ttyUSB0")

i01 = Runtime.start("i01","InMoov")
i01.startHead("/dev/ttyACM0")

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

oculus = Runtime.start("oculus","OculusDIY")

def onOculusData(data):

  i01.head.neck.moveTo(int(data.pitch))
  i01.head.rothead.moveTo(int(data.yaw))

def onMyoData(myodata):
  if (myodata.currentPose == WAVE_OUT):
     mL.move(0.3)
     mR.move(0.3)
  elif :
     mL.move(0.0)
     mR.move(0.0)

oculus.addOculusDataListener(python)
myo.addMyoDataListener(python)
remote.startListening()

