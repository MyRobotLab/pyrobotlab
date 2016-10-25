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

# start the jaw control for animation while speaking
i01.startMouthControl(comPort)

# the position for the jaw to be open/closed during annimzation.
openPosition = 20
closedPosition = 90
i01.mouthControl.setmouth(openPosition, closedPosition)

# say hello world and annimate the response.
i01.mouth.speak("Welcome to my breakdown.")
i01.head.neck.moveTo(90)
i01.head.rothead.moveTo(90)

sleep(2)

i01.mouth.speak("I hope I didn't scare you.")
i01.head.neck.moveTo(0)
i01.head.rothead.moveTo(0)


