# Script to change the voulme of the Max8744
# It's similar to the pcf8574 in that it only writes a single byte
# The voume is controlled by writing a value between 0 and 63
volume = 16
arduino = Runtime.start("arduino","Arduino")
arduino.connect("COM8")
max = Runtime.start("max9744","Pcf8574")
max.setController(arduino,"0","0x4B")
max.writeRegister(volume)
