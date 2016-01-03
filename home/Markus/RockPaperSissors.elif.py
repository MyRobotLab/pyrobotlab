 i01.mouth.speak("no points")
            sleep(1)
    if inmoov == 3:
        stoprockpaperscissors()
        sleep(1)
    elif human == 3:                       # changed from if to  elif               
        stoprockpaperscissors()
        sleep(1)
    elif inmoov <= 2:                      # changed from if to  elif  
        rockpaperscissors2()
    elif human <= 2:                       # changed from if to  elif  
        rockpaperscissors2()    
 
def stoprockpaperscissors():
    rest()
    sleep(5)
    if inmoov < human:
        i01.mouth.speak("congratulations you won with" + str(human - inmoov) + "points")
        sleep(3)
        i01.mouth.speak(str(human) + "points to you and" + str(inmoov) + "points to me")
    elif inmoov > human:                                                                                                         # changed from if to  elif 
        i01.mouth.speak("yes yes i won with" + str(inmoov - human) + "points")
        sleep(3)
        i01.mouth.speak("i've got " + str(inmoov) + "points and you got" + str(human) + "points")
    elif inmoov == human:                                                                                                          # changed from if to  elif 
        i01.mouth.speak("none of us won we both got" + str(inmoov) + "points")
    global inmoov
    inmoov = 0
    global human
    human = 0
    i01.mouth.speak("that was fun")
    sleep(2)
    i01.mouth.speak("do you want to play again")
    sleep(10)
    data = msg_i01_ear_recognized.data[0]
    if (data == "yes let's play again"):
        rockpaperscissors2()
    elif (data == "yes"):                                                                              # changed from if to  elif 
        rockpaperscissors2()
    elif (data == "no thanks"):                                                                  # changed from if to  elif 
        i01.mouth.speak("maybe some other time")
        sleep(4)
        powerdown()
    elif (data == "no thank you"):                                                           # changed from if to  elif 
        i01.mouth.speak("maybe some other time")
        sleep(4)
        powerdown()
    ##i01.mouth.speak("ok i'll find something else to do then")
    ##lookaroundyou()