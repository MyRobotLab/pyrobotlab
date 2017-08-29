# Import Java Runtime, but call it "oscmd" to avoid conflict with MRL Runtime 
from java.lang import Runtime as oscmd
process = oscmd.getRuntime().exec("notepad.exe")
