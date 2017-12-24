################################################
#  Artifitial Inteligents Markup Language 
#  OOB
################################################
# this file is more of a place holde as it is not yet 
# ready but is called by the MainCommandFile.py
#
# This file will handle all of the OOB data sent by 
# the ProgramAB Service.

def onText(data):
     print data
     if (data == "light on"):
         lightOn()
     elif (data == "light off"):
         lightOff()
 
#fred.addOOBTextListener("publishText","python","onText")
#fred.publishOOBText(data)
