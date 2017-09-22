#########################################
# ImageDisplay.py
# description: used as a general template
# more info @: http://myrobotlab.org/service/ImageDisplay
#########################################
 
#Display an image as it is. The string might be an internet source or path to an image on the computer.
imagedisplay = Runtime.start("imagedisplay","ImageDisplay")
imagedisplay.display("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg")
sleep(2)
#Closes all active images.
imagedisplay.closeAll()

#Display an image while fading it in at the beginning.
imagedisplay.displayFadeIn("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg")
sleep(2)
imagedisplay.closeAll()

#Display an image faded by a given value between 0 and 1.
imagedisplay.display("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg", 0.1)
sleep(2)
imagedisplay.closeAll()

#Display an image scaled by a given multiplication factor.
imagedisplay.displayScaled("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg", 2)
sleep(2)
imagedisplay.closeAll()

#Display an image faded faded by a given value between 0 and 1 and scaled by a given multiplication factor.
imagedisplay.displayScaled("http://www.iep.utm.edu/wp-content/media/Zeno_of_Elea-200x300.jpg", 0.1 ,2)
sleep(2)
imagedisplay.closeAll()

#Display an image in FullScreen Mode (Fullscreenmode can be terminated with a mouseclick.
imagedisplay.displayFullScreen("https://upload.wikimedia.org/wikipedia/commons/f/fe/Escher_Cube.png")
sleep(2)
imagedisplay.closeAll()

#Display an image in FullScreen Mode faded by a given value between 0 and 1. (Fullscreenmode can be terminated with a mouseclick.
imagedisplay.displayFullScreen("https://upload.wikimedia.org/wikipedia/commons/f/fe/Escher_Cube.png", 0.1)
sleep(2)
#Method to exit Fullscreen but keep the image.
imagedisplay.exitFS()
sleep(2)
imagedisplay.closeAll()

#Get the resolutions of the current Display.
print (imagedisplay.getResolutionOfW())
print (imagedisplay.getResolutionOfH())

