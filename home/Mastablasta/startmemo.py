import random
from java.lang import String
from org.myrobotlab.net import BareBonesBrowserLaunch
holygrail = Runtime.createAndStart("holygrail", "WebGui")
wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
elias = Runtime.createAndStart("elias", "ProgramAB")
elias.startSession("ProgramAB", "MastaBlasta", "elias")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
wksr.addTextListener(elias)
elias.addTextListener(htmlfilter)
htmlfilter.addTextListener(mouth)

meco1 = 0
meco2 = 0
meco3 = 0

def COUNTER1():
    global meco1
    meco1 = meco1 + 1
    if (meco1 == 4):
       resp = elias.getResponse("RETRIGGER1")

def COUNTER2():
    global meco2
    meco2 = meco2 + 1
    if (meco2 == 4):
       resp = elias.getResponse("RETRIGGER2")

def COUNTER3():
    global meco3
    meco3 = meco3 + 1
    if (meco3 == 4):
       resp = elias.getResponse("RETRIGGER3")

def GETMEMO():
    resp = elias.getResponse("MEMOTRIGGER")
