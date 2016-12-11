arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM7")
arduino1 = Runtime.createAndStart("arduino1","Arduino")
arduino1.setBoardAtmega328()
 
#connecting arduino1 to arduino Serial1 instead to a COMX
arduino1.connect(arduino,"Serial1") 
servo = Runtime.createAndStart("servo","Servo")
servo.attach(arduino1,5)
 
#attaching procedure take a bit more time to do, wait a little before using it
sleep(1)
servo.moveTo(90)
