i01 = Runtime.createAndStart("i01", "InMoov")

unoPort = "COM4"

# create parts rather than start them
# so that they may be customized before starting
head = i01.createPeer("head")

# all these services were created with the
# i01.createPeer("head") - but we want a referenced handle on them
# so we can customize parameters
jaw = head.createPeer("jaw")
eyeX = head.createPeer("eyeX")
eyeY = head.createPeer("eyeY")
rothead = head.createPeer("rothead")
neck = head.createPeer("neck")
uno = head.createPeer("arduino")

uno.connect(unoPort)

# starting parts
# i01.startMouthControl(unoPort)
# i01.startMouth()
#to tweak the default voice
# i01.mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Ryan&txt=")

# custom pins - must be done before
# starting

jaw.setPin(7)
eyeX.setPin(8)
eyeY.setPin(9)
rothead.setPin(10)
neck.setPin(11)

i01.startHead(unoPort)

# other customizations can be called
# at anytime ...
# setting new min and max limits
# this will prevent jaw from moving past
jaw.setMinMax(20, 154)
# mapping is different than setting the min & max
# min & max work as clipping functions
# mapping maps the whole range of the first two values onto
# the second - so its more like "volume control" instead
rothead.map(0,180,10,160)
