from java.lang import String
from time import sleep

arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("COM8") 

m1 = Runtime.start("m1","Motor")
m1.setType2Pwm(10,11)
m1.attach(arduino)

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addCommand("Links", "python", "Links", "Links")
keyboard.addCommand("Rechts", "python", "Rechts", "Rechts")

def Links(cmd):
    global keyboardInput
    keyboardInput = "Links"
    print "motor left"
    m1.move(1.0)
    sleep(1)
    m1.move(0.0)

def Rechts(cmd):
    global keyboardInput
    keyboardInput = "Rechts"
    print "motor right"
    m1.move(-1.0)
    sleep(1)
    m1.move(0.0)
