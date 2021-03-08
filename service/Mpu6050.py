#########################################
# Mpu6050.py
# more info @: http://myrobotlab.org/service/Mpu6050
#########################################
# port = "/dev/ttyUSB0"
port = "COM3"

mpu6050 = Runtime.createAndStart("Mpu6050","Mpu6050")
# start optional virtual arduino service, used for test
# virtual = True
if ('virtual' in globals() and virtual):
    virtualArduino = Runtime.start("virtualArduino", "VirtualArduino")
    virtualArduino.connect(port)
# end test
# raspi controler :
# raspi = Runtime.createAndStart("RasPi","RasPi")
arduino = Runtime.start("arduino","Arduino")
arduino.connect(port)
# on a raspi you may need to search both buses to find
# your device e.g.
# sudo i2cdetect -y 0
# sudo i2cdetect -y 1
# mpu6050.attach(raspi,"0","0x68")
mpu6050.attach(arduino,"1","0x68")
mpu6050.refresh()
print mpu6050.filtered_x_angle
print mpu6050.filtered_y_angle
print mpu6050.filtered_z_angle
