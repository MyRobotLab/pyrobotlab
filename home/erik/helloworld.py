arduino = Runtime.start("arduino","Arduino")
servo1 = Runtime.start("servo1","Servo")
arduino.serial.refresh()
sleep (1)

arduino.serial.connect("COM3")

sleep(1)

servo1.attach(arduino,13)

servo1.moveTo(20)

sleep(2)

servo1.moveTo(120)

sleep(2)

servo1.moveTo(90)
