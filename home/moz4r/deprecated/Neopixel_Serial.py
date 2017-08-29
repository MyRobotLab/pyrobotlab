#Just a poc maybe there is a best method
#Flash Neopixel_MRL.ino
import time
serial = Runtime.createAndStart("serial","Serial")
Runtime.createAndStart("mouth", "AcapelaSpeech")
serial.connect("COM7", 9600, 8, 1, 0)
sleep(5)
mouth.speak("Hi everybody this is neo pixel ring controled by my robot lab")
sleep(3)
mouth.speak("Fire, It burn a lot")
serial.write(2) 
sleep(6)
mouth.speak("Hello jarvis")
serial.write(3)
sleep(6)
mouth.speak("I am a cylon")
serial.write(1)
sleep(6)
serial.write(9)
