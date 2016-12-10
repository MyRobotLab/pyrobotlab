import csv
import datetime

logfile = csv.writer(open(basePath+"\\mrl-script\\pinocchio\\aiml.log","ab"))

def aimlLog(data):
  now = datetime.datetime.now()
  time = now.strftime("%Y-%m-%d %H:%M")
  logfile.writerow([time,language,data])