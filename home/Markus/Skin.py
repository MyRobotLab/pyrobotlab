from time import sleep
from org.myrobotlab.service import Speech
 
 
# Name it "speech".
speech = Runtime.create("speech","Speech")
speech.startService()
serial1 = Runtime.start('serial1','Serial')
serial2 = Runtime.start('serial2','Serial')
 
speech.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Laura&txt=") 
 
speech.speak("hello")
 
serial1.connect('COM8')
serial2.connect('COM6')

# this subscribe is easy shorthand method
# python.subscribe('serial1','publishRX')
# python.subscribe('serial2','publishRX')
# this subscribe with 4 parameters has all details - subscribe to and callback info
# we subscribe to one service's topic to one method and the other to a different method
python.subscribe('serial1','publishRX', python.getName(), 'serial1RX'); 
python.subscribe('serial2','publishRX', python.getName(), 'serial2RX'); 
 
#  i want this to be the data from serial1
 
def serial1RX(data):
    print(data)
    num = data
    #num = chr(data)
    #print(num)
    if (num == 1):
       speech.speak("1")
    if (num == 2):
       speech.speak("2")
    if (num == 3):
       speech.speak("3")
    if (num == 4):
       speech.speak("4")         
    if (num == 5):
       speech.speak("5")
    if (num == 6):
       speech.speak("6")
    if (num == 7):
       speech.speak("7")
    if (num == 8):
       speech.speak("8")
    if (num == 9):
       speech.speak("9")
    if (num == 10):
       speech.speak("10")
    if (num == 11):
       speech.speak("11")
    if (num == 12):
       speech.speak("12")
 
#  and this to be the data from serial2
 
def serial2RX(data):
    print(data)
    num = data
    #num = chr(data)
    #print(num)
    if (num == 1):
       speech.speak("1")
    if (num == 2):
       speech.speak("2")
    if (num == 3):
       speech.speak("3")
    if (num == 4):
       speech.speak("4")         
    if (num == 5):
       speech.speak("5")
    if (num == 6):
       speech.speak("6")
    if (num == 7):
       speech.speak("7")
    if (num == 8):
       speech.speak("8")
    if (num == 9):
       speech.speak("9")
    if (num == 10):
       speech.speak("10")
    if (num == 11):
       speech.speak("11")
    if (num == 12):
       speech.speak("12")
