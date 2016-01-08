#script to control the TrashyBot platform through remote control via Xbox 360 wireless remote
#
#
#Nolan B. 1/8/16


from org.myrobotlab.service import Joystick
from org.myrobotlab.service import Arduino
from org.myrobotlab.service import Runtime
from time import sleep

#----------------------------------Web Gui--------------------------
webgui = Runtime.create("webgui", "WebGui")
webgui.autoStartBrowser(False)
Runtime.start("webgui", "WebGui")


#---------------------------------Create Services----------------------
arduino = Runtime.createAndStart("arduino","Arduino")
joystick = Runtime.createAndStart("joystick","Joystick")
motorL = Runtime.start("motorL","Motor")
motorR = Runtime.start("motorR","Motor")
log = Runtime.start("log","Log")



#----------------------Connect Peripherals-----------------------------------
joystick.setController(0); #PC only - Pi needs new
joystick.addInputListener(python)
arduino.connect("/dev/ttyACM0");
# Tell the joystick to turn on
joystick.startPolling()


# attach servos to Arduino
arduino.motorAttach("motorL", 5, 4) 
arduino.motorAttach("motorR", 6, 7) 

#Detach for safety


#------------------------DEFINE STATICVALUES--------------------------


#----------------------Define callback function for Joystick-----------
def onJoystickInput(data):  
  if (data.id == 'A' and float(data.value) == 1.0):
    AttatchAll(1)
  if (data.id == 'B' and float(data.value) == 1.0):
    DetatchAll(1)
  if (data.id == 'ry') and float(data.value == 1.0):
      motorL.move(1)
      motorR.move(1)
  if (data.id == 'ry') and float(data.value == -1.0):
      motorL.move(-1)
      motorR.move(-1)
  if (data.id == 'ry') and float(data.value == 0.0):
      motorL.stop()
      motorR.stop()
  if (data.id == 'rx') and float(data.value == 1.0):
      motorL.move(-1)
      motorR.move(1)
  if (data.id == 'rx') and float(data.value == -1.0):
      motorL.move(1)
      motorR.move(-1)
  if (data.id == 'rx') and float(data.value == 0.0):
      motorL.stop()
      motorR.stop()


#-----------------------------SERVO ACTION----------------------------------------

#----------------------------------Saftey Locks------------------------------------

