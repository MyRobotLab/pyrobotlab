servoPin01 = 4
port = "COM3"
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")
arduino.connect(port)
servo01.attach(arduino.getName(), servoPin01)
servo01.moveTo(90)
