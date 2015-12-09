arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/ttyACM0")

remote = Runtime.start("remote","RemoteAdapter")
neck = Runtime.createAndStart("neck","Servo")
rothead = Runtime.createAndStart("rothead", "Servo")

sleep(1)

neck.attach(arduino,12)
rothead.attach(arduino,13)

neck.setMinMax(10,170)
rothead.setMinMax(10,170)

neck.setInverted(True)
rothead.setInverted(True)

oculus = Runtime.start("oculus","OculusDIY")

def onOculusData(data):

  neck.moveTo(int(data.pitch))
  rothead.moveTo(int(data.yaw))

oculus.addOculusDataListener(python)
remote.startListening()
