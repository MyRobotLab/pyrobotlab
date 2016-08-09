taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
java -jar myrobotlab.jar -install
java -jar myrobotlab.jar -invoke python execFile %cd%/1-INMOOV-AI_startup.py -service GUIService GUIService python Python