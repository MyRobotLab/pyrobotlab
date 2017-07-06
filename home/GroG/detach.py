port = "COM99"
virtual = Runtime.start('virtual','VirtualArduino')
virtual.connect(port)
adafruit = Runtime.start('adafruit','Adafruit16CServoDriver')
arduino = Runtime.start('arduino','Arduino')
arduino.connect(port)
