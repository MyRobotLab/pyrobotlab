#!/usr/bin/python

"""Notifies myself of IP change."""
import smtplib
import requests
import yagmail
import os
import urllib2

# Import the email modules we'll need
from email.mime.text import MIMEText

ADDRESS_FILE = '/tmp/old_ip_address.txt'

def notify_ip_change(newIp):

    # msg = MIMEText("Alert! The server's IP has changed to %s" % newIp)

    contents = urllib2.urlopen("http://build.myrobotlab.org:8888/setIpAddress?ipaddress=" + newIp).read()

    # yagmail.SMTP('supertick@gmail.com').send('supertick@gmail.com', "ip " + newIp)

    # sender = 'work-e@myrobotlab.org'
    # recipient = 'supertick@gmail.com'
    # msg['Subject'] = 'Alert - IP address has changed'
    # msg['From'] = sender
    # msg['To'] = recipient

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    # s = smtplib.SMTP('localhost')
    # s.sendmail(sender, recipient, msg.as_string())
    # s.quit()
# [notify_if_change ends]


def detect_ip_change():
    blnDelta = False
    currIp = requests.get('https://api.ipify.org').text

    if not os.path.isfile(ADDRESS_FILE):
        # trigger the script to send email for the first time
        persist_ip('127.0.0.1')

    oldIp = read_old_ip()

    if currIp != oldIp:
        blnDelta = True

    persist_ip(currIp)
    return (blnDelta, currIp)
# [detect_ip_change ends]


def persist_ip(ip):
    f = open(ADDRESS_FILE, 'w')
    f.write(ip)
    f.close()
# [persist_ip ends]


def read_old_ip():
    f = open(ADDRESS_FILE, 'r')
    oldIp = f.read()
    f.close()
    return oldIp
# [read_old_ip ends]


# [START main]
def main():
    deltaTuple = detect_ip_change()
    if deltaTuple[0] is True:
        notify_ip_change(deltaTuple[1])
        print "IP changed. Email sent!"
    else:
        print "No news is good news."
# [END main]


if __name__ == '__main__':
    main()
    
