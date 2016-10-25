from time import sleep

# The com port
comPort = "COM5"

# create the inmoov service
i01 = Runtime.createAndStart("i01", "InMoov")

i01.setMute(True)

# start the mouth to be able to speak
i01.startMouth()

# start the head service
i01.startHead(comPort)

# Re-assign the pins for the servos.

rotheadPin = 44
neckPin = 28
jawPin = 48 

# first detach them.. 
i01.head.rothead.detach()
i01.head.neck.detach()
i01.head.jaw.detach()
# now , attach them with the right pin number
i01.head.rothead.attach(rotheadPin)
i01.head.neck.attach(neckPin)
i01.head.jaw.attach(jawPin)


# update min/max values to be 0 - 180 ..
i01.head.rothead.setMinMax(0,180)
i01.head.neck.setMinMax(0,180)

# start the jaw control for animation while speaking
i01.startMouthControl(comPort)

# the position for the jaw to be open/closed during annimzation.
openPosition = 20
closedPosition = 90
i01.mouthControl.setmouth(openPosition, closedPosition)

# say hello world and animate the response.
i01.mouth.speak("Welcome to my breakdown.")
i01.head.neck.moveTo(90)
i01.head.rothead.moveTo(90)

sleep(2)

i01.mouth.speak("I hope I didn't scare you.")
i01.head.neck.moveTo(0)
i01.head.rothead.moveTo(0)


