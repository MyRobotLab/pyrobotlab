import random

from org.myrobotlab.service import Speech
mouth = Runtime.createAndStart("mouth","Speech")

mem = 0


for y in range(0, 10):
    x = (random.randint(1 ,5))
    if x == mem:
        if mem == 5:
            global x
            x -= 1
        else :
            global x
            x += 1
    global mem
    mem = x
    if x == 1:
        mouth.speak("1")
        global mem
        mem = 1
        print mem
        sleep (1.5)
    if x == 2:
        mouth.speak("2")
        global mem
        mem = 2
        print mem
        sleep (1.5)
    if x == 3:
        mouth.speak("3")
        global mem
        mem = 3
        print mem
        sleep (1.5)
    if x == 4:
        mouth.speak("4")
        global mem
        mem = 4
        print mem
        sleep (1.5)
    if x == 5:
        mouth.speak("5")
        global mem
        mem = 5
        print mem
        sleep (1.5)
    
