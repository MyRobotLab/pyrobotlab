
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")


import time 
millis = time.time()



def input(cmd):
    global millis
    # print 'python object is',msg_[service]_[method]
    cmd = msg_keyboard_keyCommand.data[0]
#    print 'python data is', cmd

    if (cmd == "A"):
       interval = time.time() -  millis
       millis = time.time()
       print ("sleep(" + str(interval) + ")")