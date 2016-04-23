# this program show how to use wikidata fetcher with programAB


import random
import codecs
import socket
from java.lang import String

chatBot=Runtime.createAndStart("chatBot", "ProgramAB")
ear=Runtime.createAndStart("ear", "WebkitSpeechRecognition")
mouth=Runtime.createAndStart("mouth", "AcapelaSpeech")
htmlFilter=Runtime.createAndStart("htmlFilter", "HtmlFilter")
webgui=Runtime.createAndStart("webgui", "WebGui")

chatBot.startSession("ProgramAB", "default", "wikidata")
wdf=Runtime.createAndStart("wdf", "WikiDataFetcher") 
wdf.setLanguage("en") # we are using english word
wdf.setWebSite("enwiki") # we are looking for datas in english database
sleep(2)
mouth.setLanguage("EN") 
mouth.setVoice("Ryan") 
ear.addTextListener(chatBot) 
ear.setLanguage("en-EN")
chatBot.addTextListener(htmlFilter) 
htmlFilter.addListener("publishText", python.name, "talk") 

def talk(data):
	if data!="":
		mouth.speak(data)
  		print "chatbot :", data
  		
def askWiki(query):
	query = unicode(query,'utf-8') # query is the subject
	print query
	word = wdf.cutStart(query) # removing the start ( "the moon" -> "moon")
	# start = wdf.grabStart(query) # keep only the start ( "the moon" -> "the") // i don't remember why i needed that ! but it exist ...
	wikiAnswer = wdf.getDescription(word)
	answer = ( query + " is " + wikiAnswer)
	if wikiAnswer == "Not Found !":
		answer = "I don't know"
	chatBot.getResponse("say " + answer)

def getProperty(query, what):
	query = unicode(query,'utf-8') # query is the subject (adam sandler, eiffel tower, moon)
	what = unicode(what,'utf-8') # what is the data that we are looking for ( birthdate, high, birth place ...)
	ID = "error"
	# the file properties_ID.txt contain the mapping from "what" to "ID" (money -> P38)
	# this file is used instead of the "map" folder in programAB because programAB mapping seem dosn't manage accents 
	f = codecs.open(u"C:/Users/papa/git/pyrobotlab/home/beetlejuice/properties_ID.txt",'r',"utf-8") # set you propertiesID.txt path !!
	for line in f:
    		line_textes=line.split(":")
    		if line_textes[0]== what:
	    		ID= line_textes[1]
	f.close()
	
	print "query = " + query + " - what = " + what + " - ID = " + ID # print some variable to help find errors
	wikiAnswer= wdf.getData(query,ID)
	answer = ( what +" of " + query + " is " + wikiAnswer)
	
	if wikiAnswer == "Not Found !":
		answer = "I don't know"
	chatBot.getResponse("say " + answer)
	return answer

def getDate(query, ID): # this function return a custom display
	answer = ( wdf.getTime(query,ID,"day") +" " +wdf.getTime(query,ID,"month") + " " + wdf.getTime(query,ID,"year"))
	print " the date is : " + answer
	chatBot.getResponse("say The " + answer)

	