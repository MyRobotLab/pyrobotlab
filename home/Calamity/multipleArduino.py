arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM15")

arduino1 = Runtime.createAndStart("arduino1","Arduino")
arduino1.setBoardUno()
#connecting arduino1 to arduino Serial1 instead to a COMX
arduino1.connect(arduino,"Serial1") 

servo = Runtime.createAndStart("servo","Servo")
servo.attach(arduino1,5)

servo.moveTo(90)
