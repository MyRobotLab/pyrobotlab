taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
cd "C:\inmoov MRL"
java -jar myrobotlab.jar -service gui GUIService python Python -invoke python execFile C:\github\pyrobotlab\home\brotherbrown831\inmoov\marvin_pro_head.py
