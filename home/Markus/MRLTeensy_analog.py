from time import sleep
from org.myrobotlab.service import Speech
 
 
# Name it "speech".
speech = Runtime.create("speech","Speech")
speech.startService()
serial = Runtime.start('serial','Serial')
 
speech.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Laura&txt=") 
 
speech.speak("hello")
 
serial.connect('COM6')
 
python.subscribe('serial','publishRX')
 
def publishRX(data):
    print(data)
    num = data
    #num = chr(data)
    #print(num)
    if (num == 1):
       speech.speak("one")
    if (num == 2):
       speech.speak("two")
    if (num == 3):
       speech.speak("three")
    if (num == 4):
       speech.speak("four")         
    if (num == 5):
       speech.speak("five")
    if (num == 6):
       speech.speak("six")
    if (num == 7):
       speech.speak("seven")
    if (num == 8):
       speech.speak("eight")
    if (num == 9):
       speech.speak("nine")
    if (num == 10):
       speech.speak("ten")
    if (num == 11):
       speech.speak("eleven")
    if (num == 12):
       speech.speak("twelve") 
