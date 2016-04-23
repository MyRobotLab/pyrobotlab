#PICTURE FIND AND DISPLAY BOT
#LONK AT http://www.myai.cloud/
#FOR SERVER NAME AND BOT STATUS
#IT S A SMALL COMPUTER FOR NOW SORRY IF PROBLEMS
from java.lang import String
import random
import threading
import itertools

http = Runtime.createAndStart("http","HttpClient")
Runtime.createAndStart("chatBot", "ProgramAB")
Runtime.createAndStart("ear", "WebkitSpeechRecognition") 
Runtime.createAndStart("webGui", "WebGui")
Runtime.createAndStart("htmlFilter", "HtmlFilter")
Runtime.createAndStart("mouth", "AcapelaSpeech")  
Runtime.createAndStart("Image", "ImageDisplay") 

mouth.setVoice("Ryan")
mouth.setLanguage("EN")
#mouth.setVoice("Antoine")
#mouth.setLanguage("FR")

chatBot.startSession( "default", "rachel") 
chatBot.addTextListener(htmlFilter) 
htmlFilter.addListener("publishText", python.name, "talk") 

def talk(data):
	mouth.speak(data)
  	print "chatbot dit :", data
def FindImage(image):
	mouth.speak("I show you "+image)
  #mouth.speak("Voici "+image)
	#PLEASE USE REAL LANGUAGE PARAMETER :
	#lang=XX ( FR/EN/RU/IT etc...)
	#A FAKE LANGUAGE WORKS BUT DATABASE WILL BROKE
	a = String(http.get("http://myai.cloud/bot1.php?pic="+image.replace(" ", "%20")+"&lang=US"))
	#a = String(http.get("http://myai.cloud/bot1.php?pic="+image.replace(" ", "%20")+"&lang=FR"))
	Image.display(a)
