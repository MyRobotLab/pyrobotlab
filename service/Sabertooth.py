saber = Runtime.start('saber','Sabertooth')
saber.connect(port)
sleep(1)

for x in range(0,120):
  saber.driveForwardMotor1(x)

sleep(1)

for x in range(120, -1, -1):
  saber.driveForwardMotor1(x)
