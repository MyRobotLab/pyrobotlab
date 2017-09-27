#########################################
# VirtualServo.py
# one virtual servo to control them all ( useful for no hacked servos )
#########################################
# uncomment for virtual hardware
# virtual = True

servoPin01 = 4
servoPin02 = 5

# port = "/dev/ttyUSB0"
port = "COM15"


# start optional virtual arduino service, used for test
# virtual=True
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)

virtualServoControllerVirtual = Runtime.start("virtualServoControllerVirtual", "VirtualArduino")
virtualServoControllerVirtual.connect("COM42")
virtualServoController = Runtime.start("virtualServoController","Arduino")
virtualServoController.connect("COM42")

arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")
virtualServo = Runtime.start("virtualServo","Servo")

# initialize arduino
# arduino.connect("/dev/ttyUSB0")
arduino.connect(port)

# attach servo
servo01.attach(arduino.getName(), servoPin01)
servo02.attach(arduino.getName(), servoPin02)
virtualServo.attach(virtualServoController.getName(), 2)


virtualServo.eventsEnabled(True);
virtualServo.addListener("publishServoEvent",python.name,"onServoEvent")

def onServoEvent(position):
    servo01.moveTo(position)
    servo02.moveTo(180-position)
    if not virtualServo.isMoving():
      servo01.broadcastState()
      servo02.broadcastState()
