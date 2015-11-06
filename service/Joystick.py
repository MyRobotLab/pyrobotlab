joy = Runtime.createAndStart("joy","Joystick")

joy.setController(2)

joy.addInputListener(python)

def onJoystickInput(data):
 print data
