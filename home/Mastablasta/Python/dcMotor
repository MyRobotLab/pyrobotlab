from java.lang import String
arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect("COM8") 
m1 = Runtime.createAndStart("m1","Motor")
m1.attach("COM8", "TYPE_2_PWM", 5, 6);

keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addCommand("Links", "python", "Links", "Links")
keyboard.addCommand("Rechts", "python", "Rechts", "Rechts")

def Links(cmd):
    global keyboardInput
    keyboardInput = "Links"
    print "motor left"
    m1.move(0.5)
    sleep(2)
    m1.stop()

def Rechts(cmd):
    global keyboardInput
    keyboardInput = "Rechts"
    print "motor right"
    m1.move(-0.8)
    sleep(2)
    m1.stop()
    
