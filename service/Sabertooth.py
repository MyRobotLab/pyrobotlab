#########################################
# Sabertooth.py
# categories: motor
# more info @: http://myrobotlab.org/service/Sabertooth
#########################################
# uncomment for virtual hardware
from org.myrobotlab.service import Serial
virtual = True

# sabertooth serial port - if on windows might be COM4
port = "/dev/ttyUSB0"

# controller index for the joystick
controllerIndex = 0

# start optional virtual serial service, used for test
if ("virtual" in globals() and virtual):
    # use static method Serial.connectVirtualUart to create
    # a virtual hardware uart for the serial service to
    # connect to
    uart = Serial.connectVirtualUart(port)
    uart.logRecv(True) # dump bytes sent from sabertooth

# start the services
sabertooth = Runtime.start("sabertooth","Sabertooth")
m1 = Runtime.start("m1","MotorPort")
m2 = Runtime.start("m2","MotorPort")
joy = Runtime.start("joy","Joystick")
joy.setController(controllerIndex)

# configure services
m1.setPort("m1")
m2.setPort("m2")

# attach services
sabertooth.attach(m1)
sabertooth.attach(m2)
m1.attach(joy.getAxis("y"))
m1.attach(joy.getAxis("rz"))

# FIXME - sabertooth.attach(motor1) & sabertooth.attach(motor2)
# FIXME - motor1.attach(joystick) !
sabertooth.connect(port)

m1.stop();
m2.stop();

def autoTest():
    # speed up the motor
    for x in range(0,100):
      pwr = x * .01
      print('power ', pwr)
      m1.move(pwr)
      sleep(0.01)

    sleep(1)

    # slow down the motor
    for x in range(100, -1, -1):
      pwr = x * .01
      print('power ', pwr)
      m1.move(pwr)
      sleep(0.01)

    # move motor clockwise
    m1.move(0.3)
    sleep(1)
    m1.stop()

    # move motor counter-clockwise
    m1.move(-0.3)
    sleep(1)
    m1.stop()
