taskkill.exe /F /IM java.exe
taskkill.exe /F /IM javaW.exe
taskkill.exe /F /IM chrome.exe
RMDIR /S /Q .myrobotlab
RMDIR /S /Q haarcascades
RMDIR /S /Q hogcascades
RMDIR /S /Q lbpcascades
RMDIR /S /Q libraries
RMDIR /S /Q pythonModules
RMDIR /S /Q repo
RMDIR /S /Q resource
RMDIR /S /Q tessdata
del ivychain.xml
del myrobotlab.log
del repo.json
java -jar myrobotlab.jar -invoke python execFile %cd%/INMOOV-AI_install.py -service GUIService GUIService python Python