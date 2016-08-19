#!/usr/bin/env python
import subprocess

def cmdSms(number,text):
  subprocess.call("cd /home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/selenium && gnome-terminal -x python clickbuttonMighty.py " + str(number) + " " + str(text), shell=True)



 
