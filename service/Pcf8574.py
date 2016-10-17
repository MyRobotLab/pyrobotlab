# Initiate the Arduino
arduino = Runtime.createAndStart("Arduino","Arduino")
arduino.connect("COM3")
# Select the Arduino as controller for the IO extender on bus 1 and i2c address 0x38
pcf = Runtime.createAndStart("Pcf","Pcf8574")
pcf.setController(arduino,"1","0x38")
# Set four pins as output. 
pcf.pinMode(0,"OUTPUT")
pcf.pinMode(1,"OUTPUT")
pcf.pinMode(2,"OUTPUT")
pcf.pinMode(3,"OUTPUT")
# Blink a LED on pin 1
pcf.write(1,1)
sleep(1)
pcf.write(1,0)
sleep(1)
pcf.write(1,1)
sleep(1)
pcf.write(1,0)
sleep(1)
pcf.write(1,1)
# Set four pins as output. 
pcf.pinMode(4,"INPUT")
pcf.pinMode(5,"INPUT")
pcf.pinMode(6,"INPUT")
pcf.pinMode(7,"INPUT")
# Read and display digital input
print pcf.read(4)
print pcf.read(5)
print pcf.read(6)
print pcf.read(7)



