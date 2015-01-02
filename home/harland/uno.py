i01 = Runtime.createAndStart("i01", "InMoov")

# create parts rather than start them
# so that they may be customized before starting
head = i01.createPeer("head")
jaw = head.createPeer("jaw")
eyeX = head.createPeer("eyeX")
eyeY = head.createPeer("eyeY")
rothead = head.createPeer("rothead")
neck = head.createPeer("neck")



# starting parts
i01.startMouthControl(leftPort)
i01.startMouth()
#to tweak the default voice
i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")
i01.startHead(leftPort)
