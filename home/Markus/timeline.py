import time 
millis = time.time()
 
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")
 
 
def input(cmd):
    global millis
    if (cmd == "A"):
       interval = time.time() -  millis
       millis = time.time()
       print ("sleep(" + str(round(interval,2)) + ")")
