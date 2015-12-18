arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/ttyACM0")

i01 = Runtime.start("i01","InMoov")
i01.startHead("/dev/ttyACM0")

remote = Runtime.start("remote","RemoteAdapter")
myo = Runtime.start("myo","MyoThalmic")
mL = Runtime.start("mL","Motor")
mR = Runtime.start("mR","Motor")
mL.setType2Pwm(5,10)
mR.setType2Pwm(6,11)
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
     m1.move(0.2)

oculus.addOculusDataListener(python)
remote.startListening()
