from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Servo
from org.myrobotlab.service import Runtime
from time import sleep

# create the services

arduino = Runtime.createAndStart("arduino","Arduino")
mouth = Runtime.createAndStart("mouth","Servo")
eyes_ud = Runtime.createAndStart("eyes_ud","Servo")
eyes_lr = Runtime.createAndStart("eyes_lr","Servo")
joystick = runtime.createAndStart("joystick","Joystick")
joystick.setController(3) # Set controller index
joystick.startPolling() # Start the polling of the device this

# initialize arduino
arduino.setSerialDevice("COM4", 115200, 8, 1, 0)

# attach servo
arduino.attach("mouth",10)
arduino.attach("eyes_ud",11)
arduino.attach("eyes_lr",9)

# servo position at start
mouth.moveTo(120)
sleep(0.5)
eyes_ud.moveTo(90)
sleep(0.5)
eyes_lr.moveTo(90)
sleep(0.5)

# Joystick

b = 90
c = 80

 
def x():
    global b
    x = msg_joystick_XAxisRaw.data[0]
    print x
    if ( x > 0 ) :
     b = (130 - 60 ) * x + 90
     roundB = int(b)
     eyes_lr.moveTo(roundB)
     print roundB
    elif ( x < 0 ) :
     b = (130 - 60 ) * x + 90
     roundB = int(b)
     eyes_lr.moveTo(roundB)
     print roundB
    if (b > 129 ):
     b = 130
    if (b < 61 ):
     b = 60
    return

def y():
    global c
    y = msg_joystick_YAxisRaw.data[0]
    print y
    if ( y > 0 ) :
     c = (115 - 45 ) * y + 80
     roundC = int(c)
     eyes_ud.moveTo(roundC)
     print roundC
    elif ( y < 0 ) :
     b = (115 - 45 ) * y + 80
     roundC = int(c)
     eyes_ud.moveTo(roundC)
     print roundC
    if (c > 114 ):
     c = 115
    if (c < 24 ):
     c = 25
    return
    
def a():
    a = msg_joystick_button0.data[0]
    print a
    if (a == 1):
     mouth.moveTo(95)
    elif ( a == 0):
     mouth.moveTo(125)
 
#create a message route from joy to python so we can listen for button
joystick.addListener("XAxisRaw", python.name, "x")
joystick.addListener("button0", python.name, "a")
joystick.addListener("YAxisRaw", python.name, "y")
