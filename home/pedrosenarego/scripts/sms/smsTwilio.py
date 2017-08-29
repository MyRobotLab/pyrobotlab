from twilio.rest import TwilioRestClient
import sys
ACCOUNT_SID = 'ACd19a4a789e0ec06207fb838288308b07'
AUTH_TOKEN = '102895919403cf08b1a452276dd6204a'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
NUMBER = sys.argv[1]
TEXT = sys.argv[2]+"\n\nSent from my robot Zorba"
client.messages.create(
    to = str(NUMBER),
    from_ = '+15676860831',
    body = str(TEXT),
)

