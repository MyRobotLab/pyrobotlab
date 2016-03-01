import time 

 
keyboard = Runtime.createAndStart("keyboard", "Keyboard")
keyboard.addListener("keyCommand", python.getName(), "input")

on = 0

##################################################################
 
 
def input(cmd):


            
    if (cmd == "C"):
        global on 
        on = 1
        while on == 1:
            print (on)
            sleep (1)
 

    if (cmd == "B"):
        global on 
        on = 0    
