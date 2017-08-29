# Dans le repertoire "myrobotlab/programAB/bots" , creez un dossier au nom de votre chatbot (pour moi Sweety)
# Puis dans ce dossier, creez un nouveau dossier nomme "aiml" . Enfin placez votre/vos fichiers AIML dedans
# Au premier lancement, programAB creera d'autre dossier dans le dossier du chatbot, pas de souci c est normal
# Vous pouvez tester avec ce petit fichier qui et le premier que j ai fais pour Sweety : 
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/beetlejuice/AIML/sweety.aiml
# Aller on s amuse ! dans chrome, cliquez sur "ear" dans le menu , choisissez "francais" puis un petit clic sur le micro
# et on dit "bonjour","salut","quel est mon nom","je m appelle ...
# 


# On creer et on demarre les services
Runtime.createAndStart("chatBot", "ProgramAB") # ProgramAB qui lit et interprete les fichiers AIML
Runtime.createAndStart("ear", "WebkitSpeechRecognition") # La reconnaissance vocale ( necessite le navigateur Chrome par default )
Runtime.createAndStart("webGui", "WebGui") # Webgui "installe" MRL dans une page Web
Runtime.createAndStart("mouth", "AcapelaSpeech") # AcapelaSpeech ce connecte net et rapatrie les texte converti en mp3
Runtime.createAndStart("htmlFilter", "HtmlFilter") # htmlFilter nettoye le texte AIML en retirant les balises avant de le lire

mouth.setLanguage("FR") # on parle francais !
mouth.setVoice("Antoine") # on choisis une voix ( voir la liste des voix sur http://www.acapela-group.com/?lang=fr
chatBot.startSession( "default", "Sweety") # on demarre la session qui est dans le dossier sweety

ear.addTextListener(chatBot) # On creer une liaison de webKitSpeechRecognition vers Program AB
ear.setLanguage("fr-FR")
chatBot.addTextListener(htmlFilter) # On creer une liaison de Program AB vers html filter
htmlFilter.addListener("publishText", python.name, "talk") # On creer une liaison de htmlfilter vers mouth

chatBot.setPredicate("default","prenom","unknow") # Ca c est pour moi, j efface le nom de l interlocuteur en debut de session

def talk(data):
	mouth.speak(data)
  	print "chatbot dit :", data
