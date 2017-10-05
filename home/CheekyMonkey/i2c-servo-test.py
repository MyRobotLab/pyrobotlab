#adafruit16c servo driver servo sweep test
#undock the myrobotlab servo gui tab for your convenience :)
#
#Author: Acapulco Rolf
#Date: October 4th 2017
#Build: myrobotlab development build version 2560

from time import sleep

adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver");

#start a Raspberry Pi instance
raspi = Runtime.createAndStart("RasPi","RasPi");

#attach the AdaFruit16C I2C servo driver to the Raspberry Pi
adaFruit16c.setController("RasPi","1","0x40");

#set the frequency for the AdaFruit16C I2C servo driver to 50 Hz
adaFruit16c.setPWMFreq(0,50);

#define a pin to attach servo to
servoPin = 0
servo = Runtime.createAndStart("servo","Servo");

#attach servo to servoPin, centre servo at 90 degree, set servo to move with maximum velocity (-1)
servo.attach(adaFruit16c,servoPin,70,-1);
#update servo GUI with current servo position
servo.broadcastState()

#move servo to the 5 degree position
servo.moveTo(5)
#update servo GUI with current servo position
servo.broadcastState()

#sweep servo from 5 to 170 degrees in 5 degree increments
for i in range (5,170,5):
	servo.moveTo(i)
	#sleep for a bit	
	sleep(0.5)
	#update servo GUI with current servo position
	servo.broadcastState()
	#sleep for a bit
	sleep(0.5)

#sweep servo from 170 to 5 degrees in 5 degree increments
for i in range (170,5,-5):
	servo.moveTo(i)
	#sleep for a bit	
	sleep(0.5)
	#update servo GUI with current servo position
	servo.broadcastState()
	#sleep for a bit
	sleep(0.5)

servo.moveTo(5)
servo.broadcastState()
