#########################################
# AdafruitIna219.py
# description: Adafruit INA219 Voltage and Current sensor Service
# categories: [sensor]
#########################################
# This script shows how to use the AdafruitIna219 service
#
# This section shows is if you use the Arduino i2c pins
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM3")
raspi = Runtime.createAndStart("RasPi","RasPi")
ina219 = Runtime.createAndStart("AdafruitIna219","AdafruitIna219")
ina219.setController(arduino,"1","0x40")
# 
# This section shows is if you use the GPIO i2c pins on the RaspBerry Pi directly
raspi = Runtime.createAndStart("RasPi","RasPi")
ina219 = Runtime.createAndStart("AdafruitIna219","AdafruitIna219")
ina219.setController(raspi,"1","0x40")
#
# This sections shows how to get the values from the service
ina219.refresh()
print ina219.busVoltage," mV bus voltage"
print ina219.shuntResistance, "Ohms shunt resistance"
print ina219.shuntVoltage ," mV accross the shunt resistor"
print ina219.current, " mA current"
print ina219.power, " mW power"
