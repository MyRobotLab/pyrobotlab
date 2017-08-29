import csv

f = open("Index.csv", "rb")
reader = csv.reader(f, delimiter='\t', lineterminator='\n',)
columns = list(reader)

print(columns)
#indexarino = ((100-columns)*1.8)
#servo01.moveTo(indexarino)   
  
# set the servo pin that we'll control
servoPin = 3
# specify a rest postion for the servo
restPosition = 90
# specify a com port for the arduino
comPort = "/dev/ttyACM0"

# create the servo & arduino services
arduino = Runtime.start("arduino","Arduino")
servo01 = Runtime.start("servo01","Servo")

arduino.connect(comPort)
# TODO - set limits
servo01.setMinMax(0, 180)
servo01.map(0, 180, 0, 180)
servo01.setVelocity(-1)
# attach servo
servo01.attach(arduino.getName(), servoPin)
# lets move the servo to it's rest position.

servo01.moveTo(columns)
sleep(0.5)
