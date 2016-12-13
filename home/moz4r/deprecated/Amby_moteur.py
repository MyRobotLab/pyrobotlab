from time import sleep

arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.serial.refresh()
sleep(1)
arduino.connect("COM6") 
sleep(1)
arduino.publishState()
arduino.digitalWrite(3,255)

moteur = Runtime.start("moteur","Motor")
moteur.setType2Pwm(4,5)
moteur.attach(arduino)

moteur.move(1)
sleep(2)
moteur.move(0.0)
sleep(2)
moteur.move(-1)
sleep(2)
moteur.move(0.0)