# getting analog input back from arduino into Python

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.connect("COM15")

readAnalogPin = 1
readDigitalPin = 7

# make friendly sample rate
arduino.setSampleRate(8000)

# add call back route
arduino.addListener("publishPin", "python", "publishPin")

# my call-back
def publishPin(pin):
  print pin.pin, pin.value, pin.type, pin.source

# get data from analog pin for 5 seconds
arduino.analogReadPollingStart(readAnalogPin)
sleep(5)
arduino.analogReadPollingStop(readAnalogPin)  

# get data from digital pin for 5 seconds
arduino.digitalReadPollingStart(readDigitalPin)
sleep(5)
arduino.digitalReadPollingStop(readDigitalPin)  


