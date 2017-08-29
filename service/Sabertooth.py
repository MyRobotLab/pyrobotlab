<<<<<<< HEAD
# start the service
sabertooth = Runtime.start("sabertooth","Sabertooth")
=======
port = "COM19"
 
saber = Runtime.start('saber','Sabertooth')
saber.connect(port)
sleep(1)
 
for x in range(0,120):
  print('power ', x)
  saber.driveForwardMotor1(x)
  sleep(0.5)
  
sleep(1)
 
for x in range(120, -1, -1):
  print('power ', x)
  saber.driveForwardMotor1(x)
  sleep(0.5)
>>>>>>> master
