<<<<<<< HEAD
# start the service
joystick = Runtime.start("joystick","Joystick")
# print the controllers out - there may be many
# the format will be like this
# {0 - HID Keyboard Device: 0, 1 - Standard PS/2 Keyboard: 1, 2 - HID-compliant mouse: 2, 3 - Dell Touchpad: 3, 4 - 3Dconnexion KMJ Emulator: 4, 5 - Logitech Cordless RumblePad 2: 5}
# in this case I want to attach the service to the Logitech Cordless RumblePad 2, which is controller number 5
print(joystick.getControllers())
# now we'll subscribe the python to the joystick publishJoystickInput - which will make the data come back to onJoystickInput method
python.subscribe("joystick","publishJoystickInput")
joystick.setController(5)

# this is a callback method in Jython
# when data comes from the Joystick this method is called
# "data" contains and id & value - you can add if statements
# which determine which component was pressed or moved - then do
# something exciting - like move the robot left or close the gripper
def onJoystickInput(data):
  print(data, data.id, data.value)

  if data.id == u'6':
    print("button 6 is ", data.value)
  if data.id == u'z':
    print("axis z is ", data.value)
=======
joy = Runtime.createAndStart("joy","Joystick")
#this set which kind of controller you want to poll data from
#it is the number you can see in the Joystick GUI when you open the list of devices
joy.setController(2)

#tell joystick service to send data to python as a message only when new data is aviable
joy.addInputListener(python)

#this is the method in python which receive the data from joystick service
#it is triggered only when new data arrive, it's not a loop !
def onJoystickInput(data):
 #this print the name of the key/button you pressed (it's a String)
 print data.id 
 #this print the value of the key/button (it's a Float)
 print data.value
>>>>>>> master
