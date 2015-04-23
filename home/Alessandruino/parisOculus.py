oculus = Runtime.start("oculus","OculusDIY")
oculus.arduino.connect("/dev/tty.usbmodem14521")

def onOculusData(data):

  print data.yaw
  print data.pitch

oculus.addOculusDataListener(python)
