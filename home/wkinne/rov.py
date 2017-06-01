######################################################
# A script to control the ROV
######################################################

# create the arduino service
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM4")
 
# create services for the 3 motors on the rov
rightMotor = Runtime.createAndStart("rightMotor", "Motor")
leftMotor = Runtime.createAndStart("leftMotor", "Motor")
rearMotor = Runtime.createAndStart("rearMotor", "Motor")
 
# create the joystick service
joystick = Runtime.createAndStart("joystick", "Joystick")
 
# set the pins on the motors 
rearMotor.setPwrDirPins( 3, 4)
rightMotor.setPwrDirPins( 7, 8)
leftMotor.setPwrDirPins( 5, 6)

# attach the motors to the arduino so they can be controlled
rightMotor.attach(arduino)
leftMotor.attach(arduino)
rearMotor.attach(arduino)
 
# subscribe to the publishJoystickInput (this will call "onJoystickInput" in python 
python.subscribe("joystick","publishJoystickInput") 

# choose which controller
joystick.setController(3) 

# initialize the values for x and y so they're not null
x = 0
y = 0

################################################################
# This is the joystick callback method
# each button push will call this method with the button id and the value of that button..
################################################################
def onJoystickInput(data): 
  # define the x and y variables as global
  global x
  global y
  # a debug statement to print the data being returned from the joystick
  print(data, data.id, data.value)
  if data.id == u'ry':
     print("button ry is ", data.value)
  if data.id == u'rx':
     print("button rx is ", data.value)
  if data.id == u'x':
     # assign the value to the global variable "x"
     x = data.value
     print("button x is ", data.value)
  if data.id == u'y':
     # assign the joystick value to the global variable y
     y = data.value
     # print("button y is ", data.value)
  if data.id == 'z':
     print("axis z is ", data.value)
  if data.id == 'z':
     rearMotor.move(data.value)
     
  # at this point we have the latest values for x and y saved in global memory
  # compute the values to send to the motors
  lefty=y+x                  
  righty=y-x
  # send the values to the motors.
  leftMotor.move(lefty)
  rightMotor.move(righty)
 
