#from __future__ import print_function
import sys
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from oauth2client import file
from apiclient.discovery import build
from httplib2 import Http

import datetime


#try:
    #import argparse
    #flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
#except ImportError:
    #flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
  creds = tools.run_flow(flow, store, flags) \
	  if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

SUBJECT = sys.argv[1]
DATE = sys.argv[2]
START = sys.argv[3]
END = sys.argv[4]
LOCATION = sys.argv[5]

GMT_OFF = '-04:00'
EVENT = {
  'location' : LOCATION,
  'summary' : SUBJECT,
  'start' : {'dateTime': str(DATE)+'T'+str(START)+':00:00%s' % GMT_OFF},
  'end' : {'dateTime': str(DATE)+'T'+str(END)+':00:00%s' % GMT_OFF},
  'attendees': [
    
  ],
}
  
e = CAL.events().insert(calendarId='primary',
	sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
  Start: %s
  End:   %s''' % (e['summary'].encode('utf-8'),
	e['start']['dateTime'], e['end']['dateTime']))
