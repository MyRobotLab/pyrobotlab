
# this is a little script that is easy to copy and paste into your main inmoov script.

import random

music = Runtime.createAndStart("music","Speech")
music.audioFile.addListener("stopped", python.name, "stopped")

leftPort = "COM3"
rightPort = "COM7"

 
i01 = Runtime.createAndStart("i01", "InMoov")

i01.startAll(leftPort, rightPort)

torso = i01.startTorso("COM3")

left = Runtime.getService("i01.left")
right = Runtime.getService("i01.right")

####################################

musiconoff = 0

####################################

ear = i01.ear

ear.addCommand("play some music", "python", "play")

ear.addComfirmations("yes","correct","ya") 
ear.addNegations("no","wrong","nope","nah")
 
ear.startListening("play next song | turn off the music ")
 
# set up a message route from the ear --to--> python method "heard"
ear.addListener("recognized", "python", "heard")

####################################

def heard(data):
    data = msg_i01_ear_recognized.data[0]

    if (data =="play next song"):
        music.audioFile.silence()
        
    if (data =="turn off the music"):
        global musiconoff
        musiconoff = 0
        music.audioFile.silence()

####################################

def play():   
    global musiconoff
    musiconoff = 1
    number = str(random.randint(1, 314))
    i01.mouth.speak("playing song number" + str(number))
    # name your mp3 files music1 music2 and so on
    music.audioFile.playFile("C:\\Users\\Markus\\Music\\Robynsfavoriter\\music" + str(number) + ".mp3", False)
    print number



# stopped method is called when at the end of an audio file
def stopped():
    if musiconoff == 0 :
        print ("stop playing")
    elif musiconoff == 1 :
        play()

#################################### 
