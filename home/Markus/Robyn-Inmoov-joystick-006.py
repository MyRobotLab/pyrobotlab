
if voice == 0:
    i01.mouth.speak("loading joystick Script")
elif voice == 1:
    i01.mouth.speak("laddar joystick Script")


serial = Runtime.createAndStart("serial","Serial")
serial.connect('COM7')

joystick = Runtime.start("joystick","Joystick")
joystick.setController(14)

listener3 = MRLListener('publishJoystickInput', 'python', 'onJoystick1Input')
joystick.addListener(listener3)

Yval1 = 90
Yval2 = 90
Xval1 = 90
Xval2 = 90

lstest = 0
lrtest = 0
lbtest = 0
lwtest = 0

rstest = 0
rrtest = 0
rbtest = 0
rwtest = 0

def onJoystick1Input(data):

#    if (data.id== "Esc" and data.value == 1.0):
#        if drive == 0:
#            drivemode()
#        elif drive == 1:
#            gesturemode()
#        elif drive == 2:
#            autonomousmode()

    if (data.id== "z"):
        if handshake == 1:
            global test
            test = data.value * 180
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.thumb.moveTo(int(float(test2)))
            i01.rightHand.index.moveTo(int(float(test2)))
            i01.rightHand.majeure.moveTo(int(float(test2)))
            i01.rightHand.ringFinger.moveTo(int(float(test2)))
            i01.rightHand.pinky.moveTo(int(float(test2)))
        if arms == 0:
            global XboxZ
            XboxZ = ((data.value + 1) * 127)
            XboxZ = ("%.0f"%XboxZ)       
        if (arms == 1) or (arms == 2):
            global test
            test = data.value * 180
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.thumb.moveTo(int(float(test2)))
            i01.rightHand.index.moveTo(int(float(test2)))
            i01.rightHand.majeure.moveTo(int(float(test2)))
            i01.rightHand.ringFinger.moveTo(int(float(test2)))
            i01.rightHand.pinky.moveTo(int(float(test2)))
            i01.leftHand.thumb.moveTo(int(float(test2)))
            i01.leftHand.index.moveTo(int(float(test2)))
            i01.leftHand.majeure.moveTo(int(float(test2)))
            i01.leftHand.ringFinger.moveTo(int(float(test2)))
            i01.leftHand.pinky.moveTo(int(float(test2)))
        if leftarm == 1 or leftarm == 2:
            global test
            test = 180 - ((1 + data.value ) * 180)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.leftHand.thumb.moveTo(int(float(test2)))
            i01.leftHand.index.moveTo(int(float(test2)))
            i01.leftHand.majeure.moveTo(int(float(test2)))
            i01.leftHand.ringFinger.moveTo(int(float(test2)))
            i01.leftHand.pinky.moveTo(int(float(test2)))
        if rightarm == 1 or rightarm == 2:
            global test
            test = data.value * 180
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.thumb.moveTo(int(float(test2)))
            i01.rightHand.index.moveTo(int(float(test2)))
            i01.rightHand.majeure.moveTo(int(float(test2)))
            i01.rightHand.ringFinger.moveTo(int(float(test2)))
            i01.rightHand.pinky.moveTo(int(float(test2)))
                        
    if (data.id== "rx"):
        if handshake == 1:
            global test
            test = 180 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.wrist.moveTo(int(float(test2)))  
            global test
            test = (data.value + 1) * 90
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.rotate.moveTo(int(float(test2)))
        if arms == 0:
            global XboxRX
            XboxRX = (data.value + 1) * 127.5
            XboxRX = ("%.0f"%XboxRX)
        if arms == 1:
            global test
            test = (data.value + 1) * 90
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.rotate.moveTo(int(float(test2)))
            i01.leftArm.rotate.moveTo(int(float(test2)))
        if arms == 2:
            if data.value > 0.2:    
                if data.value > rrtest: 
                    global rrtest 
                    rrtest = data.value    
                    global test
                    test = (i01.rightArm.rotate.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.rotate.moveTo(int(float(test2))) 
                    test = (i01.leftArm.rotate.getPos() + 1) 
                    test2 = ("%.0f"%test) 
                    i01.leftArm.rotate.moveTo(int(float(test2))) 
                    i01.leftArm.rotate.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rrtest 
                rrtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rrtest:
                    global rrtest 
                    rrtest = data.value
                    global test
                    test = (i01.rightArm.rotate.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.rotate.moveTo(int(float(test2))) 
                    test = (i01.leftArm.rotate.getPos() - 1) 
                    test2 = ("%.0f"%test) 
                    i01.leftArm.rotate.moveTo(int(float(test2)))       
        if rightarm == 1:
            global test
            test = (data.value + 1) * 90
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.rotate.moveTo(int(float(test2)))
        if leftarm == 1:
            global test
            test = 180 - ((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.leftHand.wrist.moveTo(int(float(test2)))

        elif leftarm == 2:
            if data.value > 0.2:    
                if data.value > lwtest: 
                    global lwtest 
                    lwtest = data.value    
                    global test
                    test = (i01.leftHand.wrist.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftHand.wrist.moveTo(int(float(test2))) 
                              
            elif data.value > -0.1 and data.value < 0.1 :
                global lwtest 
                lwtest = 0 
                               
            elif data.value < -0.2:
                if data.value < lwtest:
                    global lwtest 
                    lwtest = data.value
                    global test
                    test = (i01.leftHand.wrist.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftHand.wrist.moveTo(int(float(test2))) 

        elif rightarm == 2:
            if data.value > 0.2:    
                if data.value > rrtest: 
                    global rrtest 
                    rrtest = data.value    
                    global test
                    test = (i01.rightArm.rotate.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.rotate.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rrtest 
                rrtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rrtest:
                    global rrtest 
                    rrtest = data.value
                    global test
                    test = (i01.rightArm.rotate.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.rotate.moveTo(int(float(test2))) 
            
    if (data.id== "ry"):
        if handshake == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.bicep.moveTo(int(float(test2))) 
            i01.rightArm.shoulder.moveTo(int(float(test2)))
        if arms == 0:
            global XboxRY
            XboxRY = 255 - ((data.value + 1) * 127.5)
            XboxRY = ("%.0f"%XboxRY)              
        if arms == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.shoulder.moveTo(int(float(test2)))
            i01.leftArm.shoulder.moveTo(int(float(test2)))
        if arms == 2:
            if data.value > 0.2:    
                if data.value > rstest: 
                    global rstest 
                    rstest = data.value    
                    global test
                    test = (i01.rightArm.shoulder.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.shoulder.moveTo(int(float(test2))) 
                    test = (i01.leftArm.shoulder.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.shoulder.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rstest 
                rstest = 0 
                               
            elif data.value < -0.2:
                if data.value < rstest:
                    global rstest 
                    rstest = data.value
                    global test
                    test = (i01.rightArm.shoulder.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.shoulder.moveTo(int(float(test2))) 
                    test = (i01.leftArm.shoulder.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.shoulder.moveTo(int(float(test2))) 
        if rightarm == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.shoulder.moveTo(int(float(test2)))
        if leftarm == 1:
            global test
            test = 120 - ((data.value + 1) * 90)
            test2 = ("%.0f"%test)
 #           print(test2)
            i01.leftArm.bicep.moveTo(int(float(test2)))

        elif leftarm == 2:
            if data.value > 0.2:    
                if data.value > lbtest: 
                    global lbtest 
                    lbtest = data.value    
                    global test
                    test = (i01.leftArm.bicep.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.bicep.moveTo(int(float(test2))) 
                    
            elif data.value > -0.1 and data.value < 0.1 :
                global lbtest 
                lbtest = 0 
                               
            elif data.value < -0.2:
                if data.value < lbtest:
                    global lbtest 
                    lbtest = data.value
                    global test
                    test = (i01.leftArm.bicep.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.bicep.moveTo(int(float(test2))) 

        elif rightarm == 2:
            if data.value > 0.2:    
                if data.value > rstest: 
                    global rstest 
                    rstest = data.value    
                    global test
                    test = (i01.rightArm.shoulder.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.shoulder.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rstest 
                rstest = 0 
                               
            elif data.value < -0.2:
                if data.value < rstest:
                    global rstest 
                    rstest = data.value
                    global test
                    test = (i01.rightArm.shoulder.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.shoulder.moveTo(int(float(test2))) 
                                            
    if (data.id== "y"):       
        if arms == 0 or handshake == 1:
            i01.setHeadSpeed(0.9, 0.9)
            global Yval1
            global Yval2
            test = 180 - ((data.value + 1) * 90)
            Yval1 = ("%.0f"%test)
            if (Yval1 <> Yval2) :
                Yval2 = Yval1
#                print(Yval2)               
                i01.head.neck.moveTo(int(float(Yval2)))
                i01.head.eyeY.moveTo(int(float(Yval2)))                 
        elif arms == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.bicep.moveTo(int(float(test2)))  
            i01.leftArm.bicep.moveTo(int(float(test2)))   
        elif arms == 2:
            if data.value > 0.2:    
                if data.value > rbtest: 
                    global rbtest 
                    rbtest = data.value    
                    global test
                    test = (i01.rightArm.bicep.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.bicep.moveTo(int(float(test2))) 
                    test = (i01.leftArm.bicep.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.bicep.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rbtest 
                rbtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rbtest:
                    global rbtest 
                    rbtest = data.value
                    global test
                    test = (i01.rightArm.bicep.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.bicep.moveTo(int(float(test2))) 
                    test = (i01.leftArm.bicep.getPos() + 1) 
                    test2 = ("%.0f"%test) 
                    i01.leftArm.bicep.moveTo(int(float(test2)))         
        elif leftarm == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.leftArm.shoulder.moveTo(int(float(test2))) 
        elif rightarm == 1:
            global test
            test = 120 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightArm.bicep.moveTo(int(float(test2))) 
            
        elif leftarm == 2:
            if data.value > 0.2:    
                if data.value > lstest: 
                    global lstest 
                    lstest = data.value    
                    global test
                    test = (i01.leftArm.shoulder.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.shoulder.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global lstest 
                lstest = 0 
                               
            elif data.value < -0.2:
                if data.value < lstest:
                    global lstest 
                    lstest = data.value
                    global test
                    test = (i01.leftArm.shoulder.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.shoulder.moveTo(int(float(test2))) 

        elif rightarm == 2:
            if data.value > 0.2:    
                if data.value > rbtest: 
                    global rbtest 
                    rbtest = data.value    
                    global test
                    test = (i01.rightArm.bicep.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.bicep.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rbtest 
                rbtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rbtest:
                    global rbtest 
                    rbtest = data.value
                    global test
                    test = (i01.rightArm.bicep.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightArm.bicep.moveTo(int(float(test2)))
                                 
    if (data.id== "x"):
        if arms == 0 or handshake == 1:
            i01.setHeadSpeed(0.8, 0.8)
            global Xval1
            global Xval2
            test = 180 - ((data.value + 1) * 90)
            Xval1 = ("%.0f"%test)
            if (Xval1 <> Xval2) :
                Xval2 = Xval1
#                print(Xval2)      
                i01.head.rothead.moveTo(int(float(Xval2))) 
                i01.head.eyeX.moveTo(int(float(Xval2)))         
        elif arms == 1:
            global test
            test = 180 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.wrist.moveTo(int(float(test2)))  
            i01.leftHand.wrist.moveTo(180 - int(float(test2))) 
        elif arms == 2: 
            if data.value > 0.2:    
                if data.value > rwtest: 
                    global rwtest 
                    rwtest = data.value    
                    global test
                    test = (i01.rightHand.wrist.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightHand.wrist.moveTo(int(float(test2))) 
                    test = (i01.leftHand.wrist.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftHand.wrist.moveTo(int(float(test2))) 
                    
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rwtest 
                rwtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rwtest:
                    global rwtest 
                    rwtest = data.value
                    global test
                    test = (i01.rightHand.wrist.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightHand.wrist.moveTo(int(float(test2))) 
                    test = (i01.leftHand.wrist.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftHand.wrist.moveTo(int(float(test2)))             
        elif leftarm == 1:
            global test
            test = 180 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.leftArm.rotate.moveTo(int(float(test2)))   
        elif rightarm == 1:
            global test
            test = 180 -((data.value + 1) * 90)
            test2 = ("%.0f"%test)
#            print(test2)
            i01.rightHand.wrist.moveTo(int(float(test2)))   

        elif leftarm == 2:
            if data.value > 0.2:    
                if data.value > lrtest: 
                    global lrtest 
                    lrtest = data.value    
                    global test
                    test = (i01.leftArm.rotate.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.rotate.moveTo(int(float(test2))) 
                        
            elif data.value > -0.1 and data.value < 0.1 :
                global lrtest 
                lrtest = 0 
                               
            elif data.value < -0.2:
                if data.value < lrtest:
                    global lrtest 
                    lrtest = data.value
                    global test
                    test = (i01.leftArm.rotate.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.leftArm.rotate.moveTo(int(float(test2))) 

        elif rightarm == 2:
            if data.value > 0.2:    
                if data.value > rwtest: 
                    global rwtest 
                    rwtest = data.value    
                    global test
                    test = (i01.rightHand.wrist.getPos() - 1) 
                    test2 = ("%.0f"%test)
                    i01.rightHand.wrist.moveTo(int(float(test2))) 
                           
            elif data.value > -0.1 and data.value < 0.1 :
                global rwtest 
                rwtest = 0 
                               
            elif data.value < -0.2:
                if data.value < rwtest:
                    global rwtest 
                    rwtest = data.value
                    global test
                    test = (i01.rightHand.wrist.getPos() + 1) 
                    test2 = ("%.0f"%test)
                    i01.rightHand.wrist.moveTo(int(float(test2)))
               
    if (data.id== "8" and data.value == 1.0):
        i01.mouth.speak("left")
        global leftarm
        leftarm = 2 
        global rightarm
        rightarm = 0
        global arms
        arms = 3 
        blue()

    if (data.id== "9" and data.value == 1.0):
        i01.mouth.speak("Right")
        global rightarm
        rightarm = 2 
        global leftarm
        leftarm = 0
        global arms
        arms = 3 
        blue()
        
    if (data.id== "6" and data.value == 1.0):
        if arms == 0 :
            global arms
            arms = 1
            i01.mouth.speak("arm control is activated")
        else :
            global arms
            arms = 0
            global rightarm
            rightarm = 0 
            global leftarm
            leftarm = 0
            i01.mouth.speak("deactivated arm control") 
            ledoff() 

    if (data.id== "7" and data.value == 1.0):
        i01.mouth.speak("arms") 
        global arms
        arms = 2
        global rightarm
        rightarm = 0 
        global leftarm
        leftarm = 0
                
    if (data.id== "4" and data.value == 1.0):
        if handshake == 1:
            handskak()
        if leftarm == 0 :
            global leftarm
            leftarm = 1 
            global rightarm
            rightarm = 0 
            global arms
            arms = 3 
            i01.mouth.speak("left on")
            blue()
        elif leftarm == 1 or leftarm == 2 :
            global leftarm
            leftarm = 0          
            i01.mouth.speak("left off")
#            sleep(2)
#            global arms 
#            arms = 0

    if (data.id== "0" and data.value == 1.0):
        if rightarm == 1 or rightarm == 2 or handshake == 1:
            i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() - 4) 
        elif leftarm == 1 or leftarm == 2:
            i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() + 4) 
        elif (arms == 1) or (arms == 2):
            i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() - 4) 
            i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() - 4) 

    if (data.id== "5" and data.value == 1.0):
        if handshake == 1:
            hiimrobyn()
        if rightarm == 0 and (arms == 0 or arms == 3):
            global rightarm
            rightarm = 1 
            global leftarm
            leftarm = 0
            global arms
            arms = 3 
            i01.mouth.speak("right on")
            blue()
        elif (arms == 1) or (arms == 2)  :
            arms = 3
            i01.mouth.speak("arms off")
        elif rightarm == 1 or rightarm == 2:
            global rightarm
            rightarm = 0 
            i01.mouth.speak("right off")
#            sleep(2)
#            global arms
#            arms = 0 
    if (data.id== "1" and data.value == 1.0):
        if rightarm == 1 or rightarm == 2 or handshake == 1:
            i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() + 4) 
        elif leftarm == 1 or leftarm == 2:
            i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() - 4)
        elif (arms == 1) or (arms == 2):
            i01.rightArm.omoplate.moveTo(i01.rightArm.omoplate.getPos() + 4)
            i01.leftArm.omoplate.moveTo(i01.leftArm.omoplate.getPos() + 4)
            

    if (data.id== "2" and data.value == 1.0):
        i01.torso.topStom.moveTo(i01.torso.topStom.getPos() + 2) 

    if (data.id== "3" and data.value == 1.0):
        i01.torso.topStom.moveTo(i01.torso.topStom.getPos() - 2) 

    if (data.id== "pov" and data.value == 0.25):
        askPgmAB("pov1")

    if (data.id== "pov" and data.value == 0.375):
        askPgmAB("pov2")

    if (data.id== "pov" and data.value == 0.5):
        askPgmAB("pov3")

    if (data.id== "pov" and data.value == 0.625):
        askPgmAB("pov4")

    if (data.id== "pov" and data.value == 0.75):
        askPgmAB("pov5")

    if (data.id== "pov" and data.value == 0.875):
        askPgmAB("pov6")

    if (data.id== "pov" and data.value == 1.0):
        i01.moveHead(109,24,24,109,10)
        i01.moveArm("left",5,116,26,90)
        i01.moveArm("right",95,49,164,15)
        i01.moveHand("left",0,0,0,0,0,88)
        i01.moveHand("right",180,180,180,180,180,-11)
        i01.moveTorso(60,90,90)
#        askPgmAB("pov7")  

    if (data.id== "pov" and data.value == 0.125):
        askPgmAB("pov8") 
                                    
    serial.write(XboxZ)
    serial.write(",")
    serial.write(XboxRY)
    serial.write(",")
    serial.write(XboxRX)
    serial.write("\n")


