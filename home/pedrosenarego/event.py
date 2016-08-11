from __future__ import print_function
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

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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

SUBJECT = 'teste azul'

GMT_OFF = '-04:00'
EVENT = {
  'summary' : SUBJECT,
  'start' : {'dateTime': '2016-08-12T19:00:00%s' % GMT_OFF},
  'end' : {'dateTime': '2016-08-12T22:00:00%s' % GMT_OFF},
  'attendees': [
    
  ],
}
  
e = CAL.events().insert(calendarId='primary',
	sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
  Start: %s
  End:   %s''' % (e['summary'].encode('utf-8'),
	e['start']['dateTime'], e['end']['dateTime']))
