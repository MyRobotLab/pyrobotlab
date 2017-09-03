#########################################
# ImageDisplay.py
# description: used as a general template
# more info @: http://myrobotlab.org/service/ImageDisplay
#########################################

#off course you can display local files using corect path
imagedisplay = Runtime.start("imagedisplay","ImageDisplay")
imagedisplay.display("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg")
sleep(2)
imagedisplay.closeAll()
imagedisplay.displayFullScreen("https://upload.wikimedia.org/wikipedia/commons/f/fe/Escher_Cube.png")
sleep(2)
imagedisplay.closeAll()