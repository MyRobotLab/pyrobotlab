webgui = Runtime.createAndStart("WebGui","WebGui")
raspi = Runtime.createAndStart("RasPi","RasPi")
#
mpu6050 = Runtime.createAndStart("Mpu6050","Mpu6050")
mpu6050.setController(raspi,"1","0x68")
mpu6050.refresh()
print mpu6050.filtered_x_angle
print mpu6050.filtered_y_angle
print mpu6050.filtered_z_angle
