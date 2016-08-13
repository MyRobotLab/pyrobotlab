from org.myrobotlab.service import Runtime

serial = Runtime.createAndStart("serial","Serial")
serial.connect('COM4')

joystick = Runtime.start("joystick","Joystick")
joystick.setController(0)
python.subscribe("joystick","publishJoystickInput")

def onJoystickInput(data):
     

        
    if (data.id=="R" and data.value == 1.0):
        serial.write("255,0,0\n")  

    if (data.id=="G" and data.value == 1.0):
        serial.write("0,255,0\n") 

    if (data.id=="B" and data.value == 1.0):
        serial.write("0,0,255\n") 
