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
mouth = i01.startMouth()

# next we are going to create the arduino BEFORE startMouthControl creates it
arduino = Runtime.start("i01.left","Arduino")

# now we attach the arduino to blender - creating a virtual Arduino
# and it automagically connects all the serial pipes under the hood
blender.attach(arduino)

i01.startMouthControl("MRL.0")
i01.startHead("MRL.0")

neck = Runtime.getService("i01.head.neck")
rothead = Runtime.getService("i01.head.rothead")

neck.moveTo(90)
sleep(10)

neck.setMinMax(0,180)
neck.moveTo(180)
mouth.speak("why are you people waiting?")

rothead.sweep(0, 180)
sleep(10)
neck.sweep(90, 180)
sleep(10)
rothead.stop()
neck.stop()

#neck.map(0, 180, -180, 0)
#neck.setMinMax(-360, 360)