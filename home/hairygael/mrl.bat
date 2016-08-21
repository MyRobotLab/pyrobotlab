taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
cd "C:\Myrobotlab\myrobotlab.1.0.1412\develop\ProgramAB\bots\inmoovWebKit\aimlif"
del "learnf.aiml.csv"
cd "C:\Myrobotlab\myrobotlab.1.0.1412"
java -jar myrobotlab.jar -service gui GUIService python Python -invoke python execFile C:\Users\InMoovDeep\Documents\Arduino/InMoov3.Deep.AB.V4.py
