webgui = Runtime.createAndStart("WebGui","WebGui")
raspi = Runtime.createAndStart("RasPi","RasPi")
#
mpu6050 = Runtime.createAndStart("Mpu6050","Mpu6050")
# From version 1.0.2316 use attach instead of setController
# mpu6050.setController(raspi,"1","0x68")
mpu6050.attach(raspi,"1","0x68")
mpu6050.refresh()
print mpu6050.filtered_x_angle
print mpu6050.filtered_y_angle
print mpu6050.filtered_z_angle
