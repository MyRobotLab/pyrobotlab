port = "COM99"
virtual = Runtime.start('virtual','VirtualArduino')
virtual.connect(port)
adafruit = Runtime.start('adafruit','Adafruit16CServoDriver')
arduino = Runtime.start('arduino','Arduino')
servo = Runtime.start('servo','Servo')
arduino.connect(port)
adafruit.setController(arduino,"0","0x40")
servo.attach(adafruit,3) 
# Now close the GUI
