# start the service
varduino = Runtime.start("varduino","VirtualArduino")
# this connects the virtual emulator to 
# COM5.UART port which in turn is connected to COM5
# which that Arduino service will be connected to
varduino.connect("COM5")

# Runtime.start("webgui","WebGui")
varduino = Runtime.start("varduino","VirtualArduino")

# start the Arduino service
arduino = Runtime.start("arduino","Arduino")
# connect it to the emulator
arduino.connect("COM5")