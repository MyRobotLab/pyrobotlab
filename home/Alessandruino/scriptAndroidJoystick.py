from org.myrobotlab.math import Mapper


mapperJoystickX = Mapper (-1.0,1.0, -0.1,0.1)
mapperJoystickY = Mapper (1.0,-1.0,-0.3,0.3)

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("/dev/cu.wchusbserial1450")

remote = Runtime.start("remote","RemoteAdapter")
myo = Runtime.start("myo","MyoThalmic")
joystick = Runtime.start("joystick","Joystick")
mL = Runtime.start("mL","Motor")
mR = Runtime.start("mR","Motor")
mR.setPwmPins(6,5)
mL.setPwmPins(10,11)
mL.attach(arduino);
mR.attach(arduino);

sleep(1)

def onJoystickInput(joystickdata):
    global speed
    global turn
    global total
    if (joystickdata.id == "y"):
        speed = mapperJoystickY.calc(joystickdata.value)
    elif (joystickdata.id == "x"):
        turn = mapperJoystickX.calc(joystickdata.value)
    mL.move(speed + turn)
    mR.move(speed - turn)


joystick.addInputListener(python)
remote.startListening()
