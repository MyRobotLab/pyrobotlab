arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardNano()
arduino.connect("COM6")
arduino.setAref("DEFAULT")
def publishPin(pins):	  
	for pin in range(0, len(pins)):print(pins[pin].value)
arduino.addListener("publishPinArray","python","publishPin")
#arduino.enablePin(pinAddress, rate)
#analog pin range are 14-18 on uno, 54-70 on mega
#rate is the number of polling / sec
arduino.enablePin(14, 1)
