taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
java -jar myrobotlab.jar -service python Python webGui WebGui -invoke python execFile %cd%/RACHEL_startup.py
