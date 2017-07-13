webgui = Runtime.createAndStart("WebGui","WebGui")
ard = Runtime.createAndStart("Arduino","Arduino")
ard.connect("COM3")
#
i2cmux = Runtime.createAndStart("i2cMux","I2cMux")
# From version 1.0.2316 use attach instead of setController
i2cmux.setController(ard,"1","0x70")
i2cmux.attach(ard,"1","0x70")
#
mpu6050_0 = Runtime.createAndStart("Mpu6050-0","Mpu6050")
mpu6050_0.attach(i2cmux,"0","0x68")

mpu6050_1 = Runtime.createAndStart("Mpu6050-1","Mpu6050")
mpu6050_1.attach(i2cmux,"1","0x68")
