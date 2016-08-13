#!/usr/bin/env python
import subprocess

def runEvent(subject):
  subprocess.call("cd /home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/googlecalandar && gnome-terminal -x python event.py " + str(subject), shell=True)


runEvent("It's party time!")


 
