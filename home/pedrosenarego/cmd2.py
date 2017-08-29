#!/usr/bin/env python
import subprocess

def cmd(subject):
  subprocess.call("cd /home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/googlecalandar && gnome-terminal -x python event1.py " + str(subject), shell=True)



 
