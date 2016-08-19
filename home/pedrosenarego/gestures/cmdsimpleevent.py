#!/usr/bin/env python
import subprocess

def cmdsimpleevent(subject,data,start,end,location):
  subprocess.call("cd /home/pedro/Dropbox/pastaPessoal/3Dprinter/inmoov/scripts/googlecalandar && gnome-terminal -x python eventSimple.py " + str(subject) + " " + str(data) + " " + str(start) + " " + str(end) + " " + str(location), shell=True)



 
