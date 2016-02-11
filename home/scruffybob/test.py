wksr = Runtime.createAndStart("webkitspeechrecognition", "WebkitSpeechRecognition")
 
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
 
mouth = Runtime.createAndStart("mouth", "AcapelaSpeech")
alice = Runtime.createAndStart("alice","ProgramAB")
webGui = Runtime.createAndStart("webGui","WebGui")
 
#voices = mouth.getVoices()
mouth.setVoice("will")
 
# add a link between the webkit speech to publish to ProgramAB
wksr.addTextListener(alice)

# Add route from Program AB to html filter
alice.addTextListener(htmlfilter)

# Add route from html filter to mouth
htmlfilter.addTextListener(mouth)

# Add route from ear to mouth to keep it from talking to itself
wksr.addMouth(mouth)

python.subscribe('htmlfilter', 'publishText')
 
# talk function
def onText(sent): # this is the bit that makes the mouth move up and down 
  mouth.speak(sent)
  print ("OnText "+sent)
  ison = False
  a = sent.split()
  for word in a:
    if word[len(word)-2:] == "es" : # removing es at the end of the word
      testword = word[:-2] +'xx' # adding x's to help keep the timing
    elif word[len(word)-1:] == "e" : # removing the silant e at the end of the word
      testword = word[:-1] +'x'
    else:
      testword = word
        
    for x in range(0, len(testword)):
    
      if testword[x] in ('a', 'e', 'i', 'o', 'u', 'y' ) and ison == False :
        #arduino.digitalWrite(13, Arduino.HIGH)
        mouth.moveTo(80) # move the servo to the open spot
        ison = True
        sleep(0.15)
        mouth.moveTo(15) # close the servo 
      elif testword[x] in ('.') :
        #arduino.digitalWrite(13, Arduino.LOW)
        
        ison = False
        sleep(.95)
      else: #sleep(0.5)  sleep half a second
        #arduino.digitalWrite(13, Arduino.LOW)
        
        ison = False
        sleep(0.06) # sleep half a second
  
    #arduino.digitalWrite(13, Arduino.LOW)
    
    sleep(0.08)
# end of talk function
