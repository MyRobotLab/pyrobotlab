#CREDITS : PAPAOUTAI http://myrobotlab.org/content/translate-microsoft-translator-python-azuretranslate-0

AzureTranslator=Runtime.createAndStart("AzureTranslator", "AzureTranslator")
sleep(0.1)

AzureTranslator.setCredentials(Azure_client_id,Azure_client_secret)

 
supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
    'ar' : ' Arabic',
 #   'bs-Latn' : 'Bosnian (Latin)',
 #  'bg' : 'Bulgarian',
 #   'ca' : 'Catalan',
 #   'zh-CHS' : 'Chinese (Simplified)',
 #   'zh-CHT' : 'Chinese (Traditional)',
 #   'hr' : 'Croatian',
 #   'cs' : 'Czech',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en' : 'English',
 #  'et' : 'Estonian',
 #  'fi' : 'Finnish',
    'fr' : 'French',
    'de' : 'German',
    'el' : 'Greek',
 #  'ht' : 'Haitian Creole',
 #  'he' : 'Hebrew',
 #  'hi' : 'Hindi',
 #  'mww' : 'Hmong Daw',
 #  'hu' : 'Hungarian',
 #  'id' : 'Indonesian',
    'it' : 'Italian',
 #  'ja' : 'Japanese',
 #  'sw' : 'Kiswahili',
 #  'tlh' : 'Klingon',
 #  'ko' : 'Korean',
 #  'lv' : 'Latvian',
 #  'lt' : 'Lithuanian',
 #  'ms' : 'Malay',
 #  'mt' : 'Maltese',
    'no' : 'Norwegian',
 #  'fa' : 'Persian',
 #  'pl' : 'Polish',
 #  'pt' : 'Portuguese',
 #  'ro' : 'Romanian',
 #  'ru' : 'Russian',
 #  'sr-Cyrl' : 'Serbian (Cyrillic)',
 #  'sr-Latn' : 'Serbian (Latin)',
 #  'sk' : 'Slovak',
 #  'sl' : 'Slovenian',
    'es' : 'Spanish',
    'sv' : 'Swedish',
 #  'th' : 'Thai',
 #  'tr' : 'Turkish',
 #  'uk' : 'Ukrainian',
 #  'ur' : 'Urdu',
 #  'vi' : 'Vietnamese',
 #  'cy' : 'Welsh',
 #  'yua' : 'Yucatec Maya',
}
 
male_languages = { 
    'ar' : ' Nizar',
    'da' : 'Rasmus',
    'nl' : 'Jeroen',
    'en' : 'Ryan',
    'fr' : Voice,
    'de' : 'Klaus',
    'el' : 'Dimitris',
    'it' : 'Vittorio',
    'no' : 'Olav',
    'es' : 'Antonio',
    'sv' : 'Emil',
	'ja' : 'Sakura',
}

en_languages = {
    'arab' : 'ar',
	'arabe' : 'ar',
    'danish' : 'da',
    'dutch' : 'nl',
    'english' : 'en',
	'anglais' : 'en',
    'french' : 'fr',
    'german' : 'de',
	'allemand' : 'de',
    'greek' : 'el',
    'italian' : 'it',
	'italien' : 'it',
    'norway' : 'no',
    'spanish' : 'es',
    'espagnol' : 'es',
    'sweden' : 'sv',
	'japonais' : 'ja',
	
}


					
def translateText(text,language):
	
	AzureTranslator.detectLanguage(text)
	RealLang="0"
	try:
		RealLang=en_languages[language]
	except: 
		chatBot.getResponse("AZURE_ERROR_2 "+language)
	print RealLang
	if RealLang!="0":
		AzureTranslator.toLanguage(RealLang)
		t_text=AzureTranslator.translate(text)   
		if 'Cannot find an active Azure Market Place' in t_text:
			sleep(0.5)
			t_text=AzureTranslator.translate(text)
		if 'Cannot find an active Azure Market Place' in t_text:
			chatBot.getResponse("AZURE_ERROR_1")
		else:
			mouth.setVoice(male_languages[RealLang])  
			print t_text
			talk(t_text)
			mouth.setVoice(Voice)
			
			

