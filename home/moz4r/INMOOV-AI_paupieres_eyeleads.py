from org.myrobotlab.service import Servo

PaupiereServo = Runtime.start("PaupiereServo","Servo")
PaupiereServo.setMinMax(PaupiereMIN , PaupiereMAX)
PaupiereServo.attach(right, PaupiereServoPin)


clock = Runtime.start("clock","Clock")
clock.setInterval(1000)
# define a ticktock method
def ticktock(timedata):
	PaupiereServo.moveTo(PaupiereMIN)
	sleep(0.12)
	PaupiereServo.moveTo(PaupiereMAX)
#on fait un double clignement ou pas
	if random.randint(0,1)==1:
		sleep(0.2)
		PaupiereServo.moveTo(PaupiereMIN)
		sleep(0.12)
		PaupiereServo.moveTo(PaupiereMAX)
#on redefini une valeur aleatoire pour le prochain clignement
	clock.setInterval(random.randint(10000,30000))
#create a message routes
clock.addListener("pulse", python.name, "ticktock")
# start the clock
clock.startClock()