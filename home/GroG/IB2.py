# create a Blender service, we'll call it ... blender
blender = Runtime.start("blender","Blender")

# WORKY
# i01.leftArm.bicep
# i01.leftArm.rotate
# i01.leftArm.shoulder
# i01.head.rothead

# FIXME 
# omoplate
# eyeX
# eyeY

# FIXME - make sure a no-connect is published & error'd
# connect it to Blender - blender must be running the Blender.py
# or easier yet, start blender with the Blender.blend file
# select game mode then press p with cursor over the rendering screen
if not blender.connect():
  print("could not connect to blender - is it running and did you remember to run Blender.py")
else:
  print("connected")

# create InMoov service
i01 = Runtime.start("i01","InMoov")
# mouth = i01.startMouth()

leftPort = "MRL.0"

# next we are going to create the arduino BEFORE startMouthControl creates it
arduino = Runtime.start("i01.left","Arduino")

# now we attach the arduino to blender - creating a virtual Arduino
# and it automagically connects all the serial pipes under the hood
blender.attach(arduino)

### start inmoov services ###
# i01.startMouthControl(leftPort)
head = i01.startHead(leftPort)
leftArm = i01.startLeftArm(leftPort)

## get reference handles to services to directly modify them
# left arm parts
leftBicep = Runtime.getService("i01.leftArm.bicep")
leftRotate = Runtime.getService("i01.leftArm.rotate")
leftShoulder = Runtime.getService("i01.leftArm.shoulder")
leftOmoplate = Runtime.getService("i01.leftArm.omoplate")

# head parts
jaw = Runtime.getService("i01.head.jaw")
rothead = Runtime.getService("i01.head.rothead")
neck = Runtime.getService("i01.head.neck")

#########  start mods ###################
neck = Runtime.getService("i01.head.neck")
neck.map(0,180,90,270)
neck.setMinMax(-360, 360)

leftBicep.map(0,180,0,180)
leftBicep.setMinMax(-360, 360)

jaw.setMinMax(0, 25)


def sweep():
  global leftBicep, leftRotate, leftShoulder, leftOmoplate, jaw, rothead, neck
  leftBicep.sweep(0,180)
  leftRotate.sweep(0,180)
  leftShoulder.sweep(0,180)
  leftOmoplate.sweep(0,180)

  jaw.sweep(0,180)
  rothead.sweep(0,180)
  neck.sweep(0,180)

def stop():
  global leftBicep, leftRotate, leftShoulder, leftOmoplate, jaw, rothead, neck
  leftBicep.stop()
  leftRotate.stop()
  leftShoulder.stop()
  leftOmoplate.stop()

  jaw.stop()
  rothead.stop()
  neck.stop()
