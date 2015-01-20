#  this is a test script
#  i have a folder with the mp3 files named from music1 to music8.
#  it random choses the files . no problem
#  but i want to change the sleep(120) so the next starts when the previous is finished

from java.lang import String
from org.myrobotlab.service import Speech
from org.myrobotlab.service import Sphinx
from org.myrobotlab.service import Runtime
import random

mouth = Runtime.createAndStart("mouth","Speech")

# add python as a listener of the "stopped" event from audioFile
mouth.audioFile.addListener("stopped", python.name, "stopped")

def play():
    for y in range(0, 8):
        number = str(random.randint(1, 8))
        # usually you need to escape backslash
        mouth.audioFile.playFile("C:\\Users\\Markus\\Music\\Robynsfavoriter\\music" + str(number) + ".mp3", False)
        print number
        mouth.speak("playing song number" + str(number))
        sleep(120)
        mouth.audioFile.silence()

# stopped method is called when at the end of an audio file
def stopped():
    print("I have stopped playing")

play()


