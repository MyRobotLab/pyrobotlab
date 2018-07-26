#########################################
# work-e.py
#########################################
# uncomment for virtual hardware
from org.myrobotlab.service import Serial
# virtual = True

# sabertooth serial port - if on windows might be COM4
# port = "COM14"
# port = "/dev/ttyUSB0"
# I use udev rules to always make it the same port
port = "/dev/ftdi0"

# controller index for the joystick
controllerIndex = 0

# start optional virtual serial service, used for test
if ("virtual" in globals() and virtual):
    # use static method Serial.connectVirtualUart to create
    # a virtual hardware uart for the serial service to
    # connect to
    uart = Serial.connectVirtualUart(port)
    uart.logRecv(True) # dump bytes sent from sabertooth

# TODO - list & print controllers
# TODO - list & print controllers
# TODO - list & print axis

# start the services
sabertooth = Runtime.start("sabertooth","Sabertooth")
m1 = Runtime.start("m1","MotorPort")
m2 = Runtime.start("m2","MotorPort")
webgui = Runtime.start("webgui","WebGui")
opencv = Runtime.start("opencv","OpenCV")
joy = Runtime.start("joy","Joystick")
joy.setController(controllerIndex)

# configure services
m1.setPort("m1")
m2.setPort("m2")
opencv.setFrameGrabberType("org.bytedeco.javacv.OpenKinectFrameGrabber")

# in some cases its necessary to "invert" a motor
m1.setInverted(True)
m2.setInverted(True)

# attach services
sabertooth.attach(m1)
sabertooth.attach(m2)
m1.attach(joy.getAxis("y"))
m2.attach(joy.getAxis("rz"))

# FIXME - sabertooth.attach(motor1) & sabertooth.attach(motor2)
# FIXME - motor1.attach(joystick) !
sabertooth.connect(port)

m1.stop();
m2.stop();

# good to go - play with joystick
opencv.capture()
