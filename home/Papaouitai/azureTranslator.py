import urllib, urllib2
import json

from datetime import datetime

acapelaSpeech = Runtime.createAndStart("speech", "AcapelaSpeech")
client_id = 'your client id'
client_secret = 'your client secret'
azure = Runtime.createAndStart('azure', "ProgramAB")
htmlfilter = Runtime.createAndStart("htmlfilter", "HtmlFilter")
azure.addTextListener(htmlfilter)
htmlfilter.addTextListener(acapelaSpeech)

azure.startSession('default', 'azure')

def datestring (display_format="%a, %d %b %Y %H:%M:%S", datetime_object=None):
    if datetime_object is None:
        datetime_object = datetime.utcnow()
    return datetime.strftime(datetime_object, display_format)

def get_access_token ():

    data = urllib.urlencode({
            'client_id' : client_id,
            'client_secret' : client_secret,
            'grant_type' : 'client_credentials',
            'scope' : 'http://api.microsofttranslator.com'
            })

    try:

        request = urllib2.Request('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13')
        request.add_data(data) 

        response = urllib2.urlopen(request)
        response_data = json.loads(response.read())

        if response_data.has_key('access_token'):
            return response_data['access_token']

    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print datestring(), 'Could not connect to the server:', e.reason
        elif hasattr(e, 'code'):
            print datestring(), 'Server error: ', e.code
    except TypeError:
        print datestring(), 'Bad data from server'

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
 #  'tlh-Qaak' : 'Klingon (pIqaD)',
 #  'ko' : 'Korean',
 #  'lv' : 'Latvian',
 #  'lt' : 'Lithuanian',
 #  'ms' : 'Malay',
 #  'mt' : 'Maltese',
    'no' : 'Norwegian',
 #  'fa' : 'Persian',
 #  'pl' : 'Polish',
 #  'pt' : 'Portuguese',
 #  'otq' : 'Querétaro Otomi',
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
    'fr' : 'Antoine',
    'de' : 'Klaus',
    'el' : 'Dimitris',
    'it' : 'Vittorio',
    'no' : 'Olav',
    'es' : 'Antonio',
    'sv' : 'Emil',
}
en_languages = {
    'arab' : ' ar',
    'danish' : 'da',
    'dutch' : 'nl',
    'english' : 'en',
    'french' : 'fr',
    'german' : 'de',
    'greek' : 'el',
    'italian' : 'it',
    'norway' : 'no',
    'spanish' : 'es',
    'sweden' : 'sv',
}
def print_supported_languages ():
    codes = []
    for k,v in supported_languages.items():
        codes.append('\t'.join([k, '=', v]))
    return '\n'.join(codes)

def to_bytestring (s):
    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')

def translate (access_token, text, to_lang, from_lang=None):
    if not access_token:
        azure.getResponse('Say Sorry, the access token is invalid'
    else:
        if to_lang not in supported_languages.keys():
            azure.getResponse("Say I haven't learned this language")
            print print_supported_languages()
        else:
            data = { 'text' : to_bytestring(text), 'to' : to_lang }

            #if from_lang:
                # if from_lang not in supported_languages.keys():
                #    print 'Sorry, the API cannot translate from', from_lang
                #    print 'Please use one of these instead:'
                #    print print_supported_languages()
                #    return
                #else:
            data['from'] = from_lang

            try:

                request = urllib2.Request('http://api.microsofttranslator.com/v2/Http.svc/Translate?'+urllib.urlencode(data))
                request.add_header('Authorization', 'Bearer '+access_token)

                response = urllib2.urlopen(request)
                return response.read().replace('<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">', '').replace('</string>', '')
            
            except urllib2.URLError, e:
                if hasattr(e, 'reason'):
                    print datestring(), 'Could not connect to the server:', e.reason
                elif hasattr(e, 'code'):
                    print datestring(), 'Server error: ', e.code
def translateText(text,language):
   to = en_languages[language]
   t_text = translate(get_access_token (),text,to)     
   acapelaSpeech.setVoice(male_languages[to])  
   azure.getResponse('Say '+t_text)
