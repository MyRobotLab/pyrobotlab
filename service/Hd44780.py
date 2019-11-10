#########################################
# Hd44780.py
# more info @: http://myrobotlab.org/service/Hd44780
#########################################
# uncomment for virtual hardware
# virtual = True


# port = "/dev/ttyUSB0"
port = "COM4"

# start optional virtual arduino service, used for test
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)

# Initiate the Arduino
arduino = Runtime.start("arduino","Arduino")
arduino.connect(port)

pcf = Runtime.start("pcf","Pcf8574")
pcf.attach(arduino,"1","0x27")

lcd = Runtime.start("lcd", "Hd44780")
lcd.attach(pcf)
lcd.init()
lcd.clear()
lcd.setBackLight(True)
lcd.display_string("Spot is ready !", 1)
lcd.display_string("* MyRobotLab *", 2)