i01 = Runtime.createAndStart("i01", "InMoov")
i01.startHead("COM5")

joy = Runtime.createAndStart("joy", "Joystick")

joy.setController(3)
joy.startPolling()

joy.map("rx",-1,1,-3,3)

joy.addRXListener("python","rothead")

servo = 90

def rothead(RX):
  global servo
  servo = i01.head.rothead.getPos() + RX
  i01.head.rothead.moveTo(int(servo))
