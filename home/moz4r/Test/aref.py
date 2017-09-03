Arduino = Runtime.createAndStart("arduino","Arduino")
Arduino.connect("COM8")
Arduino.setBoardNano()
 
def publishPin(pins):
    for pin in range(0, len(pins)):
        print pins[pin].address, pins[pin].value
 
Arduino.addListener("publishPinArray","python","publishPin")
Arduino.enablePin(14,2)
Arduino.setAref("INTERNAL")
