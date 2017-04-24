#stress serial R/W test to find dark matter in the universe
#and poll a pin to a serial connected arduino

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM3")

arduino1 = Runtime.createAndStart("arduino1","Arduino")

#connecting arduino1 to arduino Serial1 instead to a COMX
arduino1.connect(arduino,"Serial1") 

servo = Runtime.createAndStart("servo","Servo")
servo.attach(arduino1,5)

#attaching procedure take a bit more time to do, wait a little before using it
sleep(5)

#nooo 10000 value/second is too much !!!
def publishPinDarkMatter(pins):
  for pin in range(0, len(pins)):
    servo.map(0,180,0,pins[pin].value+1)
    servo.moveTo(pins[pin].value-1)
    
arduino1.addListener("publishPinArray",Python.getName(),"publishPinDarkMatter")
arduino1.enablePin(14,10000)
