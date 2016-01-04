# April 25,2015 pir testing on scooter
# not working
# works if you go to arduino and pick oscope and then D4 to see waveform which starts it working

i01 = Runtime.createAndStart("i01", "InMoov")

configType = 'scoot'
if configType == 'corn':
  Port = ("COM7")    #cornell
else:
  Port = "COM6"	 #port for scooter in shop
print("pir testing")

arduino = Runtime.createAndStart("arduino", "Arduino")
arduino.connect(Port)
readDigitalPin = 4
arduino.addListener("publishPin", "python", "input")
arduino.setSampleRate(8000)
i01.startPIR(Port,4)

# note parallax pir is active high, radio shack pir is active low
# scooter has radio shack pir sensor
# azul has parallax sensor
def input(pin):
  print pin.pin, pin.value, pin.type, pin.source   
  if (pin.value == 0):
       print("***    some one is here    ***")
#      arduino.digitalReadPollingStop(readDigitalPin)     #turn off pir sensor
