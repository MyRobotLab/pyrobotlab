# This is file starts and controls MRL InMoov 
# service and attaches it to the Blender virtual InMoov
# Blender (2.72b) must be running a Blender.py TCP/IP server file

vPortLeft = "vleft"
vPortRight = "vright"

###########################################################################
### special virtual blender handling - not in "regular" scripts - begin ###

# start blender service
blender = Runtime.start("blender", "Blender")

# connect blender service to running Blender (2.72b) instance
if (not blender.connect()):
	print("could not connect")

# get Blender.py version 
# FIXME - compare expected version !
blender.getVersion()

# pre-create Arduinos 
i01_left = Runtime.start("i01.left", "Arduino")
i01_right = Runtime.start("i01.right", "Arduino")

# blender "attach" will connect Arduinos with serial ports running
# over tcp/ip sockets to Blender.py
blender.attach(i01_left)
#blender.attach(i01_right)

### special virtual blender handling - not in "regular" scripts - end  ###
##########################################################################

# resume "regular" script
# connect head
i01 = Runtime.start("i01", "InMoov")
i01.startHead(vPortLeft)
i01.startLeftArm(vPortLeft)
#i01.startRightArm(vPortRight)

mc = i01.startMouthControl("vPortLeft")
speech = i01.startMouth()
speech.speak("ow my neck hurts")

# virtual InMoov config begin ##############
jaw = Runtime.getService("i01.head.jaw")
rothead = Runtime.getService("i01.head.rothead")
neck = Runtime.getService("i01.head.neck")

jaw.map(0,180,0,180)
jaw.setMinMax(0, 180)
jaw.broadcastState()

rothead.map(0,180,0,180)
rothead.setMinMax(0, 180)
rothead.broadcastState()

neck.map(0,180,0,180)
neck.setMinMax(0, 180)
neck.broadcastState()

# virtual InMoov config end ##############
