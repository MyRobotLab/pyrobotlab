i01 = Runtime.createAndStart("i01","InMoov")
i01.startHead("/dev/tty.usbmodem1411")
#i01.startLeftArm("COM5")
#leftHand = i01.startLeftHand("COM5")
#i01.leftArm.bicep.setMinMax(5,80)

#i01.leftArm.bicep.moveTo(30)

oculus = Runtime.start("oculus","OculusDIY")
oculus.arduino.connect("/dev/tty.usbmodem14541")

def onOculusData(data):

  print data.yaw
  print data.pitch

  i01.head.neck.moveTo(int(data.pitch))
  i01.head.rothead.moveTo(int(data.yaw))

oculus.addOculusDataListener(python)
