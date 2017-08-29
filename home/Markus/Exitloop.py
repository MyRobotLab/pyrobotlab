from time import sleep
 
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

loopControl = 0

##################################################################
def input(cmd):
  global loopControl
  if (cmd == "C"):
    loopControl = 1
  if (cmd == "B"):
    loopControl = 0

while True:
  if loopControl == 1:
    print "The loop is on.."
  else:
    print "the loop is off"
  sleep (1)
