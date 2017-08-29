# 
# Get a handle to python
#
python = Runtime.getService("python")
#
# Start all services
#
esp = Runtime.createAndStart("esp8266","Esp8266_01")
ads = Runtime.createAndStart("ads1115","Ads1115")
pcf = Runtime.createAndStart("pcf","Pcf8574")
arduino = Runtime.createAndStart("arduino","Arduino")
# ada = Runtime.createAndStart("ada","Adafruit16CServoDriver")
servo3 = Runtime.createAndStart("servo3","Servo")
servo8 = Runtime.createAndStart("servo8","Servo")
#
# Initiate communication to the Arduino
#
arduino.connect("COM3")
#
# Set the ip-address to the esp8266_01
#
esp.setHost("192.168.1.99")
#
# Setup hierarical routes
#
ads.setController(esp,"0","0x48")
pcf.setController(esp,"0","0x20")
# ada.setController(arduino,"0","0x40")
servo3.attach(arduino,3)
servo8.attach(arduino,8)
#
# Setup messaging routes
#
# runtime.subscribe("ads1115","0","servo3","moveTo")
# ads.enablePin(0)
# Analog inputs
def publishPin(pins):
    for pin in range(0, len(pins)):
        # print pins[pin].address, pins[pin].value
        pos = pins[pin].value * 180 / 1024
        print pin, pos
        if pin == 0:
           servo3.moveTo(pos)
        if pin == 1: 
           servo8.moveTo(pos)
# Digital inputs           
def digitalPin(pins):
    for pin in range(0, len(pins)):
        print pins[pin].address, pins[pin].value
#
ads.setSampleRate(8)
ads.addListener("publishPinArray","python","publishPin")
ads.enablePin(0)
pcf.setSampleRate(4)
pcf.addListener("publishPinArray","python","digitalPin")
pcf.enablePin(0)
