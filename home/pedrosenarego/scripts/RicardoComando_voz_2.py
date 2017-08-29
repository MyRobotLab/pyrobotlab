# inMoov Robotic arm control by a voice and manual mode
# v2.0
#
# Ricardo Silvestre
# Clube de Robotica FabLab Barreiro
# http://roboticafablabbarreiro.blogspot.pt/
# robotica.fablabbarreiro@gmail.com 
#
# cc Attribution-ShareAlike 4.0 International


#Set arduino servo pins
servoPin01 = 2 
servoPin02 = 3
servoPin03 = 4
servoPin04 = 5
servoPin05 = 6
servoPin06 = 7

#Set servos max and min
servo01Max = 180
servo01Min = 0
servo02Max = 180
servo02Min = 0
servo03Max = 180
servo03Min = 0
servo04Max = 180
servo04Min = 0
servo05Max = 180
servo05Min = 0
servo06Max = 180
servo06Min = 0

#Set arduino com port
# comPort = "/dev/ttyUSB0"
comPort = "COM9"

##Keywords
#Mão Direita
rHandAbrir_keyw = "abrir"
rHandFechar_keyw = "fechar"
rHandCentro_keyw = "centro"
rHandMetal_keyw = "metal"
rHandDedo_keyw = "dedo"
rHandEsquerda_keyw = "esquerda"
rHandDireita_keyw = "direita"
rHandGosto_keyw = "gosto"
rHandContar_keyw = "contar"

# create the services

webkitspeechrecognition = Runtime.start("webkitspeechrecognition","WebkitSpeechRecognition")
arduino = Runtime.start("arduino","Arduino")
speech = Runtime.start("speech","AcapelaSpeech")
webgui = Runtime.start("webgui","WebGui")

# initialize arduino
arduino.connect(comPort)

servo01 = Runtime.start("servo01","Servo")
servo01.attach(arduino.getName(), servoPin01)

servo02 = Runtime.start("servo02","Servo")
servo02.attach(arduino.getName(), servoPin02)

servo03 = Runtime.start("servo03","Servo")
servo03.attach(arduino.getName(), servoPin03)

servo04 = Runtime.start("servo04","Servo")
servo04.attach(arduino.getName(), servoPin04)

servo05 = Runtime.start("servo05","Servo")
servo05.attach(arduino.getName(), servoPin05)

servo06 = Runtime.start("servo06","Servo")
servo06.attach(arduino.getName(), servoPin06)

#Set speech recognition Language
webkitspeechrecognition.setLanguage("pt-PT")

#Set voice
speech.setVoice("Celia")


#Attach servos function (in test)
def rHandAttach():
  servo01.attach(arduino.getName(), servoPin01)
  servo02.attach(arduino.getName(), servoPin02)
  servo03.attach(arduino.getName(), servoPin03)
  servo04.attach(arduino.getName(), servoPin04)
  servo05.attach(arduino.getName(), servoPin05)
  servo06.attach(arduino.getName(), servoPin06)

#Detach servos function (in test)  
def rHandDetach():
  servo01.detach()
  servo02.detach()
  servo03.detach()
  servo04.detach()
  servo05.detach()
  servo06.detach()


#Function open hand  
def rHandAbrir():
  rHandAttach()
  servo01.moveTo(servo01Min)
  servo02.moveTo(servo02Min)
  servo03.moveTo(servo03Min)
  servo04.moveTo(servo04Min)
  servo05.moveTo(servo05Min)
  rHandDetach()

#Function close hand    
def rHandFechar():
  rHandAttach()
  servo01.moveTo(servo01Max)
  servo02.moveTo(servo02Max)
  servo03.moveTo(servo03Max)
  servo04.moveTo(servo04Max)
  servo05.moveTo(servo05Max)
  rHandDetach()

#Function make metal sign
def rHandMetal():
  servo01.moveTo(servo01Max)
  servo02.moveTo(servo02Min)
  servo03.moveTo(servo03Max)
  servo04.moveTo(servo04Max)
  servo05.moveTo(servo05Min)

#Function Middle finger  
def rHandDedo():
  servo01.moveTo(servo01Max)
  servo02.moveTo(servo02Max)
  servo03.moveTo(servo03Min)
  servo04.moveTo(servo04Max)
  servo05.moveTo(servo05Max)

#Function Like 
def rHandGosto():
  servo01.moveTo(servo01Min)
  servo02.moveTo(servo02Max)
  servo03.moveTo(servo03Max)
  servo04.moveTo(servo04Max)
  servo05.moveTo(servo05Max)  

#Function Rotate Wrist left  
def rHandEsquerda():
  servo06.moveTo(servo06Min)

#Function Rotate Wrist right  
def rHandDireita():
  servo06.moveTo(servo06Max)
  
#Function Fingers on center
def rHandCentro():
  servo01.moveTo(90)
  servo02.moveTo(90)
  servo03.moveTo(90)
  servo04.moveTo(90)
  servo05.moveTo(90)  

#Function Count to five  
def rHandContar():
  rHandDireita()
  rHandFechar()
  sleep(1)
  servo01.moveTo(servo01Min)
  sleep(1)
  servo02.moveTo(servo02Min)
  sleep(1)
  servo03.moveTo(servo03Min)
  sleep(1)
  servo04.moveTo(servo04Min)
  sleep(1)
  servo05.moveTo(servo05Min)
  sleep(1)

#Function go to position given (todo, filter the data)  
def rHandPos(data):
  print data  
  servo01.moveTo(int(data))
  servo02.moveTo(int(data))
  servo03.moveTo(int(data))
  servo04.moveTo(int(data))
  servo05.moveTo(int(data))
  
#Decide wich function
def onText(data):
     print data
    # speech.speakBlocking(data)
     if (data == rHandAbrir_keyw):
         print "a abrir a mao"
         speech.speakBlocking("abrir")
         rHandAbrir()
     elif (data == rHandFechar_keyw):
         print "a fechar a mao"
         rHandFechar()
     elif (data == rHandCentro_keyw):
         print "ao centro"
         rHandCentro()
     elif (data == rHandMetal_keyw):
         print "Metal"
         rHandMetal()
     elif (data == rHandDedo_keyw):
         print "Dedo do meio"
         rHandDedo()
     elif (data == rHandEsquerda_keyw):
         print "Rodar o pulso a esquerda"
         rHandEsquerda()
     elif (data == rHandDireita_keyw):
         print "Rodar o pulso a direita"
         rHandDireita()
     elif (data == rHandGosto_keyw):
         print "Gosto"
         rHandGosto()
     elif (data == rHandContar_keyw):
         print "Contar"
         rHandContar()
     elif (data >= 0 or data <= 180):
         print "ir para: "         
         rHandPos(data)

#voice recognition
webkitspeechrecognition.addListener("publishText","python","onText")