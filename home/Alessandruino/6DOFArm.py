#create arduino and servos servicesservo1.attach(arduino,2)
arduino = Runtime.createAndStart("arduino","Arduino")
servo1 = Runtime.createAndStart("servo1","Servo")
servo2 = Runtime.createAndStart("servo2","Servo")
servo3 = Runtime.createAndStart("servo3","Servo")
servo4 = Runtime.createAndStart("servo4","Servo")
servo5 = Runtime.createAndStart("servo5","Servo")
servo6 = Runtime.createAndStart("servo6","Servo")

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startMouth()
i01.startEar()

ear = i01.ear

ear.addCommand("hello world", "python", "movement1")
ear.addCommand("position two", "python", "movement2")
ear.addCommand("rest position", "python", "movement3")

 
 
ear.addComfirmations("yes", "correct", "yeah", "ya")
ear.addNegations("no", "wrong", "nope", "nah")

#set your arduino serial port here
arduino.connect("COM3")
#wait for one second for connection
sleep(1)

#attach servos to arduino pins, change pin numbers according to your setup
servo1.attach("arduino",2)
servo2.attach("arduino",3)
servo3.attach("arduino",4)
servo4.attach("arduino",5)
servo5.attach("arduino",6)
servo6.attach("arduino",7)

#define some movements in python methods
def movement1():

  servo1.moveTo(0)
  servo2.moveTo(0)
  servo3.moveTo(0)
  servo4.moveTo(0)
  servo5.moveTo(0)
  servo6.moveTo(0)

def movement2():

  servo1.moveTo(45)
  servo2.moveTo(45)
  servo3.moveTo(45)
  servo4.moveTo(45)
  servo5.moveTo(45)
  servo6.moveTo(45)

def movement3():

  servo1.moveTo(90)
  servo1.moveTo(90)
  servo2.moveTo(90)
  servo3.moveTo(90)
  servo4.moveTo(90)
  servo5.moveTo(90)
  servo6.moveTo(90)

#execute methods
movement1()
sleep(2)
movement2()
sleep(2)
movement3()
sleep(2)

# all commands MUST be before startListening  
ear.startListening()
