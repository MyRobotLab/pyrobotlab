# create a Blender service, we'll call it ... blender
blender = Runtime.start("blender","Blender")

# connect it to Blender - blender must be running the Blender.py
# or easier yet, start blender with the Blender.blend file
# select game mode then press p with cursor over the rendering screen
if not blender.connect():
  print("could not connect to blender - is it running and did you remember to run Blender.py")
else:
  print("connected")

# create InMoov service
i01 = Runtime.start("i01","InMoov")

# next we are going to create the arduino BEFORE startMouthControl creates it
arduino = Runtime.start("i01.left","Arduino")

# now we attach the arduino to blender - creating a virtual Arduino
# and it automagically connects all the serial pipes under the hood
blender.attach(arduino)

# i01.startMouthControl("MRL.0")
# i01.startHead("MRL.0")
# mouth = i01.startMouth()

neck = Runtime.start("i01.head.neck","Servo")
neck.attach(arduino, 7)


#########  start mods ###################
neck = Runtime.getService("i01.head.neck")
neck.map(0,180,90,270)
neck.setMinMax(-360, 360)

arduino01 = Runtime.getService("arduino01")
rothead = Runtime.start("i01.head.rothead", "Servo")
rothead.attach(arduino01, 8)
#rothead = Runtime.getService("i01.head.rothead")

neck.moveTo(90)
sleep(10)
