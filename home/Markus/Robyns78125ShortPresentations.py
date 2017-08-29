import random

mouth = Runtime.createAndStart("mouth","Speech")
mouth.setGoogleURI("http://thehackettfamily.org/Voice_api/api2.php?voice=Laura&txt=") 

x = (random.randint(1, 5))
if x == 1:
    mouth.speak("hello")
if x == 2:
    mouth.speak("hi")
if x == 3:
    mouth.speak("welcome") 
if x == 4:
    mouth.speak("nice to meet you")
if x == 5:
    mouth.speak("what a lovely day")

x = (random.randint(1, 5))
if x == 1:
    mouth.speak("i'm glad i have your attention")
if x == 2:
    mouth.speak("i'm robyn inmoov")
if x == 3:
    mouth.speak("my name is robyn") 
if x == 4:
    mouth.speak("i'm a inmoov robot")
if x == 5:
    mouth.speak("i'm made in sweden")

x = (random.randint(1, 5))
if x == 1:
    mouth.speak("i'm a humanoid robot")
if x == 2:
    mouth.speak("my body is made of plastic")
if x == 3:
    mouth.speak("i'm 3 d printed") 
if x == 4:
    mouth.speak("my robot lab is the software that controls me") 
if x == 5:
    mouth.speak("there are 2 arduino mega on my back") 

x = (random.randint(1, 5))
if x == 1:
    mouth.speak("i have pressure sensors on my forearms")
if x == 2:
    mouth.speak("i have cameras in my eyes")
if x == 3:
    mouth.speak("i have a kinect in my chest") 
if x == 4:
    mouth.speak("i have voice recognition") 
if x == 5:
    mouth.speak("i have mecanum wheels")

x = (random.randint(1, 5))
if x == 1:
    mouth.speak("and i have a lot of servos")
if x == 2:
    mouth.speak("and can be controlled from a keyboard")
if x == 3:
    mouth.speak("and microphones in my ears") 
if x == 4:
    mouth.speak("and i have face recognition")
if x == 5:
    mouth.speak("and a computer on my back")
      
x = (random.randint(1, 5))
if x == 1:
    mouth.speak("i can move very human like")
if x == 2:
    mouth.speak("please take a look at my mechanics")
if x == 3:
    mouth.speak("i'm a open source project") 
if x == 4:
    mouth.speak("please take a look at my electronics") 
if x == 5:
    mouth.speak("we can be friends on facebook")
      
x = (random.randint(1, 5))
if x == 1:
    mouth.speak("you can ask my maker if you have any questions")
if x == 2:
    mouth.speak("this is great")
if x == 3:
    mouth.speak("i really like being here") 
if x == 4: 
    mouth.speak("i am having so much fun") 
if x == 5:
    mouth.speak("take a look on my videos on youtube")



    
