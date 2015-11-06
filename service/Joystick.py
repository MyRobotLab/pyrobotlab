joy = Runtime.createAndStart("joy","Joystick")

joy.addInputListener(python)

def onJoystickInput(data):
 print data
