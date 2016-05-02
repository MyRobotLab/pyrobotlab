# start the service
joystick = Runtime.start("joystick","Joystick")
print(joystick.getControllers())
python.subscribe("joystick","publishJoystickInput")
joystick.setController(5)

def onJoystickInput(data):
  print(data)
