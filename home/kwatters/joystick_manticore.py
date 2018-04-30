import math

#############################################
# Start a servo and connect it to an adruino
#############################################
servoPin = 7
arduinoPort = "COM4"
servo = Runtime.createAndStart("servo", "Servo")
arduino = Runtime.createAndStart("arduino ", "Arduino")
arduino.connect(arduinoPort)
servo.setPin(servoPin)
servo.attach(arduino)

############################
# Start the Joystick service
############################
# specify which joystick to use 
joystickId = 17
uberjoy = Runtime.createAndStart("uberjoy", "Joystick")
uberjoy.setController(joystickId)
uberjoy.startPolling()

# A helper method to map a joystick value to the servo speed and direction
def StickXListener(value):
  global servo
  threshold = 0.2
  # a scaling factor for the joystick value
  gain = 100
  # many joysticks don't snap back to a true 0 position. 
  # when i let go of the xbox controller joystick, often it snaps back to center
  # and still reads about 0.17
  absValue = math.fabs(value)
  if (absValue < threshold ):
    # below the threshold, stop the servo where it is.
    servo.setVelocity(0)
    servo.moveTo(servo.pos)
    return
  else:
    # set velocity to some amount based on the joystick position
    velocity = absValue * gain
    servo.setVelocity(velocity)
    # set the direction of the movement
    if (value < 0):
      servo.moveTo(servo.min)
    else:
      servo.moveTo(servo.max)
    return

# The main callback method from the joystick service with all button data as it changes
def onJoystickInput(data):
    print "Joystick Data:" + str(data)
    if (data.id == "x"):
        StickXListener(data.value)

########################################################
# attach the python service to the published data from the joystick

uberjoy.addInputListener(python)

