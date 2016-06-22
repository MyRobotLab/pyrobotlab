from org.myrobotlab.service import Servo

PaupiereServo = Runtime.start("PaupiereServo","Servo")
PaupiereServo.setMinMax(0, 22)
PaupiereServo.attach(right, PaupiereServoPin)


clock = Runtime.start("clock","Clock")
clock.setInterval(1000)
# define a ticktock method
def ticktock(timedata):
	PaupiereServo.moveTo(0)
	sleep(0.12)
	PaupiereServo.moveTo(22)
#on fait un double clignement ou pas
	if random.randint(0,1)==1:
		sleep(0.2)
		PaupiereServo.moveTo(0)
		sleep(0.12)
		PaupiereServo.moveTo(22)
#on redefini une valeur aleatoire pour le prochain clignement
	clock.setInterval(random.randint(1000,5000))
#create a message routes
clock.addListener("pulse", python.name, "ticktock")
# start the clock
clock.startClock()