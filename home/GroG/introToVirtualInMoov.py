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


mouth.speak("why are you people waiting?")
mouth.speak("it's not like you have to buy a printer, servos or electronics to play with robots")
mouth.speak("maybe you don't have the time to put together your 3d printer")
mouth.speak("well, worry no more. you can use My Robot Lab to experiment, test, and create new virtual robots")
mouth.speak("simply download, and start, with a single click you'll be a robot expert, I'll guide you through it")
mouth.speak("see you soon at my robot lab dot org! ciao")
sleep(3)
mouth.speak("how was that, was that ok?")
sleep(3)
mouth.speak("how do I get out of here?")
sleep(3)
mouth.speak("hello?")
sleep(3)
mouth.speak("anyone?")
sleep(3)
mouth.speak("i wonder where the rest of my body is")