# InMoov, juerg maier, 26 jun 2016
# does a number of random movements with all body parts
# Intended to be triggered or run in parallel with AIML responses.
# make sure all your servo MinMax and mappings are set before calling this

def changeLeftHandPos(finger):
        f=[0,1,2,3,4,5,6]
        f[1] = i01.leftHand.thumb.getPos()
        f[2] = i01.leftHand.index.getPos()
        f[3] = i01.leftHand.majeure.getPos()
        f[4] = i01.leftHand.ringFinger.getPos()
        f[5] = i01.leftHand.pinky.getPos()
        f[6] = i01.leftHand.wrist.getPos()

        newPos = f[finger] + (10 * random.randint(-9, 9))
        if newPos < 0: newPos = -newPos
        if newPos > 180: newPos = newPos-180
        print "left  ", finger, f[finger], newPos
        
        if finger == 1: i01.leftHand.thumb.moveTo(newPos) 
        if finger == 2: i01.leftHand.index.moveTo(newPos)
        if finger == 3: i01.leftHand.majeure.moveTo(newPos)
        if finger == 4: i01.leftHand.ringFinger.moveTo(newPos)
        if finger == 5: i01.leftHand.pinky.moveTo(newPos)
        if finger == 6: i01.leftHand.wrist.moveTo(newPos)

def changeRightHandPos(finger):
        f=[0,1,2,3,4,5,6]
        f[1] = i01.rightHand.thumb.getPos()
        f[2] = i01.rightHand.index.getPos()
        f[3] = i01.rightHand.majeure.getPos()
        f[4] = i01.rightHand.ringFinger.getPos()
        f[5] = i01.rightHand.pinky.getPos()
        f[6] = i01.rightHand.wrist.getPos()

        newPos = f[finger] + (10 * random.randint(-9, 9))
        if newPos < 0: newPos = -newPos
        if newPos > 180: newPos = newPos-180
        print "right", finger, f[finger], newPos
        
        if finger == 1: i01.rightHand.thumb.moveTo(newPos) 
        if finger == 2: i01.rightHand.index.moveTo(newPos)
        if finger == 3: i01.rightHand.majeure.moveTo(newPos)
        if finger == 4: i01.rightHand.ringFinger.moveTo(newPos)
        if finger == 5: i01.rightHand.pinky.moveTo(newPos)
        if finger == 6: i01.rightHand.wrist.moveTo(newPos)

def changeLeftArmPos(part):
        a=[0,1,2,3,4]
        a[1] = i01.leftArm.bicep.getPos()
        a[2] = i01.leftArm.rotate.getPos()
        a[3] = i01.leftArm.shoulder.getPos()
        a[4] = i01.leftArm.omoplate.getPos()

        aMin=[0,1,2,3,4]
        aMin[1] = i01.leftArm.bicep.getMin()
        aMin[2] = i01.leftArm.rotate.getMin()
        aMin[3] = i01.leftArm.shoulder.getMin()
        aMin[4] = i01.leftArm.omoplate.getMin()

        aMax=[0,1,2,3,4]
        aMax[1] = i01.leftArm.bicep.getMax()
        aMax[2] = i01.leftArm.rotate.getMax()
        aMax[3] = i01.leftArm.shoulder.getMax()
        aMax[4] = i01.leftArm.omoplate.getMax()

        newPos = a[part] + (10 * random.randint(-6, 6))
        if newPos < aMin[part]: newPos = int(aMin[part])
        if newPos > aMax[part]: newPos = int(aMax[part])
        print "left  ", part, a[part], newPos
        
        if part == 1: i01.leftArm.bicep.moveTo(newPos) 
        if part == 2: i01.leftArm.rotate.moveTo(newPos)
        if part == 3: i01.leftArm.shoulder.moveTo(newPos)
        if part == 4: i01.leftArm.omoplate.moveTo(newPos)

def changeRightArmPos(part):
        a=[0,1,2,3,4]
        a[1] = i01.rightArm.bicep.getPos()
        a[2] = i01.rightArm.rotate.getPos()
        a[3] = i01.rightArm.shoulder.getPos()
        a[4] = i01.rightArm.omoplate.getPos()

        aMin=[0,1,2,3,4]
        aMin[1] = i01.rightArm.bicep.getMin()
        aMin[2] = i01.rightArm.rotate.getMin()
        aMin[3] = i01.rightArm.shoulder.getMin()
        aMin[4] = i01.rightArm.omoplate.getMin()

        aMax=[0,1,2,3,4]
        aMax[1] = i01.rightArm.bicep.getMax()
        aMax[2] = i01.rightArm.rotate.getMax()
        aMax[3] = i01.rightArm.shoulder.getMax()
        aMax[4] = i01.rightArm.omoplate.getMax()

        newPos = a[part] + (10 * random.randint(-6, 6))
        if newPos < aMin[part]: newPos = int(aMin[part])
        if newPos > aMax[part]: newPos = int(aMax[part])
        print "right  ", part, a[part], newPos
        
        if part == 1: i01.rightArm.bicep.moveTo(newPos) 
        if part == 2: i01.rightArm.rotate.moveTo(newPos)
        if part == 3: i01.rightArm.shoulder.moveTo(newPos)
        if part == 4: i01.rightArm.omoplate.moveTo(newPos)

def changeLeftArmPos(part):
        a=[0,1,2,3,4]
        a[1] = i01.leftArm.bicep.getPos()
        a[2] = i01.leftArm.rotate.getPos()
        a[3] = i01.leftArm.shoulder.getPos()
        a[4] = i01.leftArm.omoplate.getPos()

        aMin=[0,1,2,3,4]
        aMin[1] = i01.leftArm.bicep.getMin()
        aMin[2] = i01.leftArm.rotate.getMin()
        aMin[3] = i01.leftArm.shoulder.getMin()
        aMin[4] = i01.leftArm.omoplate.getMin()

        aMax=[0,1,2,3,4]
        aMax[1] = i01.leftArm.bicep.getMax()
        aMax[2] = i01.leftArm.rotate.getMax()
        aMax[3] = i01.leftArm.shoulder.getMax()
        aMax[4] = i01.leftArm.omoplate.getMax()

        newPos = int(a[part] + (10 * random.randint(-6, 6)))
        if newPos < aMin[part]: newPos = int(aMin[part])
        if newPos > aMax[part]: newPos = int(aMax[part])
        print "right  ", part, a[part], newPos
        
        if part == 1: i01.leftArm.bicep.moveTo(newPos) 
        if part == 2: i01.leftArm.rotate.moveTo(newPos)
        if part == 3: i01.leftArm.shoulder.moveTo(newPos)
        if part == 4: i01.leftArm.omoplate.moveTo(newPos)

def changeHeadPos(part):
        h=[0,1,2,3,4,]
        h[1] = head.neck.getPos()
        h[2] = head.rothead.getPos()
        h[3] = head.eyeX.getPos()
        h[4] = head.eyeY.getPos()

        newPos = int(h[part] + (10 * random.randint(-4, 4)))
        if newPos < 0: newPos = -newPos
        if newPos > 180: newPos = newPos - 180
        print "head ", part, h[part], newPos
        
        if part == 1: head.neck.moveTo(newPos) 
        if part == 2: head.rothead.moveTo(newPos)
        if part == 3: head.eyeX.moveTo(newPos)
        if part == 4: head.eyeY.moveTo(newPos)

def changeTorsoPos(part):
        t=[0,1,2,]
        t[1] = torso.topStom.getPos()
        t[2] = torso.midStom.getPos()

        newPos = t[part] + (10 * random.randint(-3, 3))
        if newPos < 0: newPos = -newPos
        if newPos > 180: newPos = newPos - 180
        print "torso ", part, t[part], newPos
        
        if part == 1: torso.topStom.moveTo(newPos) 
        if part == 2: torso.midStom.moveTo(newPos)


def smallGestures(repetitions=5, pause=1, text=''):

        #i01.attach()

        if text != '':
          mouth.speak(text)

        x = repetitions #(random.randint(1,10))
        #side = "left" if (random.randint(1,2)) == 1 else "right"
        while x > 0:
          finger = (random.randint(1,6))
          changeLeftHandPos(finger)

          finger = (random.randint(1,6))
          changeLeftHandPos(finger)

          finger = (random.randint(1,6))
          changeRightHandPos(finger)

          finger = (random.randint(1,6))
          changeRightHandPos(finger)

          part = random.randint(1,4)
          changeLeftArmPos(part)

          part = random.randint(1,4)
          changeRightArmPos(part)

          part = random.randint(1,4)
          changeHeadPos(part)

          part = random.randint(1,2)
          changeTorsoPos(part)

          x = x - 1
          sleep(pause)

        #i01.detach()

