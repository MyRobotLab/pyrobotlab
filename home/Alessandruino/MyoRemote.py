from com.thalmic.myo.enums import PoseType

remote = Runtime.start("remote","RemoteAdapter")
remote.setDefaultPrefix("raspi")
remote.connect("tcp://192.168.0.5:6767")

roll = 0.0

sleep(2)

python.send("raspiarduino", "connect","/dev/ttyUSB0")

sleep(1)
python.send("raspiarduino", "digitalWrite",2,1)
python.send("raspiarduino", "digitalWrite",3,1)
python.send("raspiarduino", "servoAttach","raspiservo",6)
python.send("raspiservo", "map",5.0,12.0,50.0,110.0)

myo = Runtime.start("myo","MyoThalmic")

myo.connect()
myo.addMyoDataListener(python)

def onMyoData(data):
  if (data.getPose() == PoseType.FIST):
    global roll
    roll = data.getRoll()
    python.send("raspiarduino", "analogWrite",5,50)
    python.send("raspiservo", "moveTo",roll)
  elif (data.getPose() ==  PoseType.WAVE_OUT):
    python.send("raspiarduino", "analogWrite",11,50)
  elif (data.getPose() == PoseType.REST):
    python.send("raspiarduino", "analogWrite",5,0)
    python.send("raspiarduino", "analogWrite",11,0)
