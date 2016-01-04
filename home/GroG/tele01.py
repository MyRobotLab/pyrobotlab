python = Runtime.createAndStart("python","Python")
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/ttyACM0")
 
remote = Runtime.start("remote","RemoteAdapter")
neck = Runtime.createAndStart("neck","Servo")
rothead = Runtime.createAndStart("rothead", "Servo")
 
sleep(1)
 
neck.attach(arduino,10)
rothead.attach(arduino,11)
 
 
oculus = Runtime.start("oculus","OculusDIY")
 
def onOculusData(data):
 
  neck.moveTo(int(data.pitch))
  rothead.moveTo(int(data.yaw))
 
oculus.addOculusDataListener(python)
remote.startListening()
