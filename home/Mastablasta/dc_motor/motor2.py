from java.lang import String
from time import sleep

arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.serial.refresh()
sleep(2)
arduino.connect("COM5") 

m1 = Runtime.start("m1","Motor")
m1.setType2Pwm(5,6)
m1.attach(arduino)

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addCommand("Links", "python", "Links", "Links")
keyboard.addCommand("Rechts", "python", "Rechts", "Rechts")

global keyboardInput

def Links(cmd):
    keyboardInput = "Links"
    print "motor left"
    m1.move(0.5)
    sleep(0.2)
    m1.move(0.0)

def Rechts(cmd):
    keyboardInput = "Rechts"
    print "motor right"
    m1.move(-0.5)
    sleep(0.2)
    m1.move(0.0)
