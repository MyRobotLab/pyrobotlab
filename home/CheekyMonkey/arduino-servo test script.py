#Arduino connection, Adafruit16C connection and Servo test script
#

from time import sleep

port = "COM4"
arduino = Runtime.start("arduino","Arduino")
arduino.connect(port)
adaFruit16c = Runtime.createAndStart("AdaFruit16C","Adafruit16CServoDriver");
adaFruit16c.setController("arduino","1","0x40");

adaFruit16c.setPWMFreq(0,50);

servoPin1 = 15
servoPin2 = 2

servo01 = Runtime.start("servo01","Servo")
servo02 = Runtime.start("servo02","Servo")

servo01.attach(adaFruit16c,servoPin1,90,-1);
servo02.attach(adaFruit16c,servoPin2,90,-1);

#servo02.sync(servo01)

def servoMoveTo(restPos,delta):
	servo01.moveTo(restPos + delta)
	#servo02.moveTo(restPos + delta)
	servo01.broadcastState()
	#servo02.broadcastState()
	
	
#servo02.addServoEventListener(servo01)
#servo02.eventsEnabled(True)
#servo01.eventsEnabled(True)
#servo02.moveTo(90)

restPos = 45
delta = 0

def moveservos1():
	for x in range (1,5):
		for i in range (10,160,5):
			servoMoveTo(restPos,i)
			#servo01.moveTo(i)
			#sleep for a bit	
			sleep(0.25)
			#update servo GUI with current servo position	
			#sleep for a bit
			sleep(0.25)

		for i in range (160,10,-5):
			servoMoveTo(restPos,i)
			#servo01.moveTo(i)
			#sleep for a bit	
			sleep(0.25)
			#update servo GUI with current servo position	
			#sleep for a bit
			sleep(0.25)

def moveservos2():
	for w in range (1,10):
		for y in range(20,160,5):
			servo01.moveTo(y)
			sleep(0.25)
			servo01.broadcastState()
		sleep(0.5)

		for y in range(160,20,-5):
			servo01.moveTo(y)
			sleep(0.25)
			servo01.broadcastState()
		sleep(0.5)


moveservos2()
