#  this is a test script
#  i have a folder with the mp3 files named from music1 to music8.
#  it random choses the files . no problem

from java.lang import String
from org.myrobotlab.service import Speech
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime
import random

mouth = Runtime.createAndStart("mouth","Speech")

music = 1

# add python as a listener of the "stopped" event from audioFile
mouth.audioFile.addListener("stopped", python.name, "stopped")

def play():
    number = str(random.randint(1, 8))
    # usually you need to escape backslash
    mouth.audioFile.playFile("C:\\Users\\Markus\\Music\\Robynsfavoriter\\music" + str(number) + ".mp3", False)
    print number
    mouth.speak("playing song number" + str(number))


# stopped method is called when at the end of an audio file
def stopped():
    if music == 1:
        print("I have started playing")
        global music
        music = 2
    elif music == 2:
        global music
        music = 1
        play()

play()
