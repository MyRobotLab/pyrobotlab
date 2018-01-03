# create services
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
python = Runtime.start("python", "Python")
keyboard = Runtime.start("keyboard", "Keyboard")
python.subscribe("keyboard", "publishMouseMoved")

servoPin = 3
servo2Pin = 4
comPort = "COM10"

# start the service
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")

arduino.connect(comPort)

servo01.setMinMax(0, 180)
servo01.attach(arduino.getName(), servoPin)
servo01.map(0,180,180,0)
#servo01.setSpeed(1.0) # set speed to 100% of full speed

servo02.setMinMax(0, 180)
servo02.attach(arduino.getName(), servo2Pin)
servo02.map(0,180,180,0)
#servo02.setSpeed(1.0) # set speed to 100% of full speed


# non blocking event example
keyboard.addKeyListener(python);

def onKey(key):
    print ("you pressed ", key)

def onMouseMoved(mouseEvent):
    x = mouseEvent.pos.x / 10
    x = ("%.0f"%x)
    y = mouseEvent.pos.y / 5.6
    y = ("%.0f"%y)
    print ("x ", x, " y ", y)
    servo01.moveTo(int(x))
    servo02.moveTo(int(y))
