#
#  This file will NOT run under MRL.   I've uploaded it to give an example
#  in Python of a face recognition algorithm.   It has the ability to normalize 
#  training pictures (including resizing, tilting, and shifting), so all the
#  training pictures are aligned to the others, making identification easier.
#
#  On recognition, it also applies a mask (essentially an oval) to attempt to
#  remove as much of the background as possible, leaving only the face.
#
#  Purpose:   Since there has been some discussion of face identification 
#  (not just face detection, but real identification), I thought I’d share what 
#  I’ve been working on.   I started this before I found out about myrobotlab, 
#  so it was originally written to be a standalone program, but I hope to incorporate 
#  the functionality into MRL in the near future.   I figured I’d get the existing code 
#  and explanation out there, so others with better programming skills can also use this 
#  as a reference point if they want to build off of what I’ve already put together.
#  
#   Caveat:   While my degrees are in Computer Science, it’s been 20 years since I did 
#   any real programming, and I’ve just recently learning Python, so some of the things 
#   may not be as efficient as they could be.
#  
#   References:   My program incorporates a lot of things that have already been done before.   
#   I don’t claim ownership of ANYTHING that hasn’t been done before, although I haven’t seen 
#   all of the elements put together quite like this before.   Most of the implementation is 
#   mine, but I’ve reused code and examples from the following places:
#
# a.	http://docs.opencv.org/2.4.8/modules/contrib/doc/facerec/index.html
# b.	https://github.com/bytefish/facerec
# c.	http://eyalarubas.com/face-detection-and-recognition.html
# d.	https://code.google.com/archive/p/visual-control/downloads
#
# Some of the features that I’ve incorporated into my program:
# a.	Face Identification using Linear Discriminant Analysis (LDA) using FisherFaces.   
#       I started using PCA - Principal Component Analysis (Eigenfaces) but found FisherFaces 
#       to be superior for the real-world environment I was going to be operating in.
#
# b.	Face normalization during the learning phase.   The program will not only detect a 
#       face, but it will also attempt to detect the components of the face like the eyes, 
#       nose and mouth.   If those can be captured, the incoming image can be rescaled so all 
#       of the stored database pictures have the eyes and mouth in almost exactly the same position.  
#
#       Also, if we know the relative position of the eyes and mouth, I can account for tilted 
#       or skewed images as well in my normalization process.   This makes recognition easier, 
#       regardless of the size or orientation of the images.   I choose to use an affine transformation 
#       for this, but you can do it anyway you wish.
#
# c.	Image masking.   One of the big things that makes face identification difficult is the 
#       noise in the picture (all of the stuff that’s not part of the face).   In my program, when 
#       creating my models for image comparison, I mask all of the pictures using essentially an oval that
#       eliminates most of the background, leaving only the main part of the face.
#
# d.    Preprocessing:   The program optionally uses TanTriggs preprocessing to reduce variance by 
#       lighting differences between images.   I’m still playing with this, so I can’t really tell 
#       if it’s better or not.
#
# e.	Variable thresholding:    The program has the ability to scale the threshold indicators.   
#       In a controlled image environment (where pictures always have the same size, orientation and 
#       lighting), you can tighten the threshold where the program will positively identify an image.   
#       In a less controlled environment, you may have to loosen the constraints for identification.   
#       The tradeoff in loosening the constraints is a higher “false positive” rate in which you mis-identifiy 
#       a face.   The alternative if the constraints are too high is that you’ll miss identifying a face 
#       that you should identify (a false negative).
#
# f.	Speech synthesis.   Since I developed this before I discovered MRL, I was working on my own 
#       speech synthesis.   If it identifies a face, it will articulate that identification.  It will 
#       also withhold repeating that same name for a while, so it doesn’t bug you to death if you’re 
#       watching it for a long time.
#
# g.	Learning mode:   The program can learn new people from a webcam.
#
# h.	GUI that includes webcam image, separate streaming windows for faces detected and faces identified, 
#       real-time adjustments.
#
# i.	The Python program currently runs under Windows 10 with Python 2.7.   I have not tried it in 
#       any other environment. I haven't included any of the Haar cascades, since they're easy to find on
#       the internet
#

from facerec.feature import Fisherfaces
from facerec.preprocessing import TanTriggsPreprocessing
from facerec.operators import ChainOperator
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
import numpy as np
from PIL import Image
import sys, os
import time
import cv2
import multiprocessing
import time
import pyttsx
import random

#
# These are the identifier thresholds used to determine when a picture is 100% verified.
# For Fisherface processing, the threshold is arbitrarily set to 500, if we're using the Tan Triggs pre-processor,
# divide the threshold by 2.5 (e.g. 200 default).  These can still be changed, but these are the defaults
TANTRIGGS_SCALER = 2.5
IDENTIFIED_THRESHOLD = 500
current_threshold = IDENTIFIED_THRESHOLD/TANTRIGGS_SCALER

#
# Maximum number of pictures to use for any particular subject.  These are sourced 
MAX_PER_SUBJECT = 10
current_max_subjects = MAX_PER_SUBJECT

#
# Various boolean flags used to turn various modes on and off
#
voice_on = True
details_on = True
bestguess_on = False
preprocess_on = True
debug_on = True
onoff = ["Off", "On"]

#
# Speech greetings
# lastgreeting is used to control how often we say something
# GREETINGTHRESHOLD is the number of seconds between utterances
#
GREETINGS = ["I spy with my little eye,", 
             "How have you been", 
             "How do you do", 
             "It's good to meet you", 
             "It's nice to meet you", 
             "Look, it's", 
             "Hey", 
             "Well, hello", 
             "What have you been up to", 
             "Hi there", 
             "Good to see you", 
             "It's been too long", 
             "What's new", 
             "How are you", 
             "I think I see", 
             "Is that", 
             "I'm pretty sure that is", 
             "That must be",
             "Do I see", 
             "Hello", 
             "What's up", 
             "You're looking good", 
             "Howdy", 
             "Good afternoon", 
             "How is it going?", 
             "How are you doing?", 
             "What's up?", 
             "What's new?",
             "Nice to see you" ]

GREETINGTHRESHOLD = 10  # The voice won't speak any faster than once every 10 seconds
GREETINGREPEAT = 60     # The voice won't repeat any person's name faster than once every 60 seconds
lastgreeting = 0        # The ID of the person we recognized last
greetingdict = dict()   # An empty dictionary used to hold all the people we've seen in the last minute

#
# The directory to the image database
#
pathdir='database/'
filterfile = 'filter.png'

#
# Face filter used to mask edges of face pictures
#
facefilter = cv2.imread(filterfile, cv2.IMREAD_GRAYSCALE)

#
# The Haar cascades used to identify bulk faces, then facial features like eyes, noses and mouths.
#
haarcascade='haarcascade_frontalface_default.xml'
eyehaarcascade='haarcascade_eye.xml'
nosehaarcascade='haarcascade_nose.xml'
mouthhaarcascade='haarcascade_mouth.xml'

#
# Miscellenous counters
#
currentwindow = 0
currentmatch = 0


#--------------------------------------------------------------------------------------------
# HELPER FUNCTIONS
#--------------------------------------------------------------------------------------------
#
# Greet people that we recognize
#
def greet(person):
    global lastgreeting, greetingdict

    current_time = time.time()
    #
    # We don't want to overwhelm the speech synthesizer, so we limit
    # to saying a specific person no more than once per minute
    # 
    # We also don't want to say anything more than once every ten seconds or so
    #
    # See if we've already announced this person
    #
    if person in greetingdict:
        last_time = greetingdict[person]
        if current_time < (last_time + GREETINGREPEAT):
            #
            # We spoke this name less too recently, just skip it this time
            #
            return
        else:
            # 
            # We've seen this person before, but it was a while ago, so we can reannounce
            greetingdict[person] = current_time
    else:
        #
        # Newly recognized person, add them to dictionary
        #
        greetingdict[person] = current_time

    if current_time > (lastgreeting + GREETINGTHRESHOLD):
        #
        # We haven't spoken recently, go ahead and give it a shot
        #
        if (voice_on):
            engine.say(GREETINGS[random.randrange(len(GREETINGS))] + ", " + person )
            engine.runAndWait()

    lastgreeting = current_time

    
#
# Read in the database of known faces
#
def read_images(path, sz=(256,256)):
    """Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y, foldernames]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
            foldernames:  The list of all names in the database
    """
    c = 0
    X,y,Z = [], [], []
    folder_names = []   # This will be the list of all known names in the database
    
    #
    # Files are in separate directories.  The directory holds the "name", each
    # of the images in the file are the samples for that name
    #
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            folder_names.append(subdirname)
            subject_path = os.path.join(dirname, subdirname)
            number_for_this_subject = len(os.listdir(subject_path))
            last_number = None
            count = 1.0
            saved = 0

            for filename in os.listdir(subject_path):
                try:
                    #
                    # Limit the number of images per person to no more than 10
                    # If there are more than 10, just take a sample of the 10
                    #
                    if int(count*current_max_subjects/number_for_this_subject) != last_number:
                        #
                        # Get the image file
                        #
                        im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    
                        #
                        # For some reason, windows sticks an indexing file into each directory
                        #
                        if filename != "Thumbs.db":
                            # resize to given size (if given)
                            if (sz is not None):
                                im = cv2.resize(im, sz)

                            im_mask = im & facefilter
                            X.append(np.asarray(im, dtype=np.uint8))
                            Z.append(np.asarray(im_mask, dtype=np.uint8))
                            y.append(c)           
                            saved += 1                 
                            
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)

                except:
                    #
                    # Ignore unreadable files
                    #
                    print "Unknown file error:", sys.exc_info()[0], im, sz
                    pass  
                last_number = int(count*current_max_subjects/number_for_this_subject)
                count += 1
                
            if debug_on:
                print saved, "images imported for subject[", c, "]: ", subdirname
            c += 1  
    return [X,y,Z, folder_names]

#
# Within an image, find the eyes using a special Haar cascade
# If we find two eyes, we can draw squares around them in the image
# We need three things passed in:
#       The original images that we can mark up - color
#       The grayscale image that is prestine that we use for recognition
#       The offset within the grayscale image where we already found the face [x, y, width, height]
# 
def find_eyes(color_image, gray_image, face_location):
        x,y,h,w = face_location

        #
        # Only look in the box where we found the face AND
        # Only look in the top 2/3 of that box for the eyes
        #
        gray_face = gray_image[y:y+h*.66, x:x+w]

        eyes = eye_cascade.detectMultiScale(gray_face)

        #
        # eyes[] is going to be a list of lists, with each one containing the x,y,h,w information for
        # each of the eyes
        #
        # Only mark the eye boxes if we find EXACTLY two eyes
        # AND the eyes are not overlapping.  This takes care of most false positives and detection of the same eye more than once
        #
        if len(eyes) == 2:
            ex0, ey0, ew0, eh0 = eyes[0]    # Coordinates for the First eye
            ex1, ey1, ew1, eh1 = eyes[1]    # Coordinates for the Second eye

            # 
            # If eyes came out in reversed order, make sure the left one is listed first
            #
            if ex0 > ex1:
                eyes = [eyes[1], eyes[0]]

            if max(0, min(ex0+ew0, ex1+eh1) - max(ex0, ex1)) == 0:
                #
                # Eyes don't overlap, so draw the boxes
                #
                eyecount=0
                for (ex,ey,ew,eh) in eyes:
                    if details_on:
                        cv2.rectangle(color_image,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),1)

                    #
                    # Now, we need to adjust so we return the ABSOLUTE position of the eye, not the relative position
                    #
                    eyes[eyecount] = [x+ex, y+ey, eh, ew]
                    eyecount += 1
                return eyes
        #
        # Either we found two valid eyes, or we return nothing
        #
        return []
          
def find_nose(color_image, gray_image, face_location):
        x,y,h,w = face_location    
        #
        #  Look only in middle 1/3 of frame for the nose
        #
        gray_face = gray_image[y+h*.33:y+h*.66, x:x+w]
        
        nose = nose_cascade.detectMultiScale(gray_face)
        #
        # Only print nose box if we find EXACTLY one nose
        #
        if len(nose) == 1 and details_on:
            for (ex,ey,ew,eh) in nose:
                cv2.rectangle(color_image,(x+ex,y+int(ey+h*.33)),(x+ex+ew,int(y+ey+eh+h*.33)),(0,255,255),1)

        return nose

            
def find_mouth(color_image, gray_image, face_location):
        x,y,h,w = face_location    
        #
        #  Right now, look in the bottom third of the frame for the mouth
        #  The mouth will be horizontally in the middle 60% of the frame and vertically in the lower 1/3 of the frame
        #
        gray_face = gray_image[y+h*.66:y+h, x+w*.20:x+w*.80]
        
        mouth = mouth_cascade.detectMultiScale(gray_face)

        #
        # Only print mouth box if we find EXACTLY one mouth
        #
        if len(mouth) == 1:
            for (ex,ey,ew,eh) in mouth:
                if details_on:
                    cv2.rectangle(color_image,(int(x+ex+w*.20),int(y+ey+h*.66)),(int(x+ex+ew+w*.20),int(y+ey+eh+h*.66)),(255,255,0),1)
                return [[int(x+ex+w*.20),int(y+ey+h*.66),ew,eh]]
        #
        # If we found none or more than one mouth, just return an empty list
        #
        return []
        
# --------------------------------------------------------------------------------------------------------
# THE MAIN PART OF THE PROGRAM IS BELOW
# --------------------------------------------------------------------------------------------------------
# Initialize the text to speech engine
#
initial_time = time.time()
print "Loading speech engine: "       
engine = pyttsx.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)
print "Load completed in {0:.2f} seconds.\n".format(time.time() - initial_time)

#
# Grab the webcam for our use
#
initial_time = time.time()
print "Appropriating webcam for video capture: "       
vc=cv2.VideoCapture(0)
print "Appropriation completed in {0:.2f} seconds.\n".format(time.time() - initial_time)

#
# Set up the Haar cascade to detect (not recognize) the faces
#
#
# We're going to use the Fisherfaces face recognition module
#

initial_time = time.time()
print "Initializing Haar cascades for face, eyes, nose and mouth detection: "
#
# This was prior to using the TanTriggsPreprocessing, we can go back
#model = PredictableModel(Fisherfaces(), NearestNeighbor())

feature = ChainOperator(TanTriggsPreprocessing(), Fisherfaces())
classifier = NearestNeighbor()
model = PredictableModel(feature, classifier)

face_cascade = cv2.CascadeClassifier(haarcascade)
eye_cascade = cv2.CascadeClassifier(eyehaarcascade)
nose_cascade = cv2.CascadeClassifier(nosehaarcascade)
mouth_cascade = cv2.CascadeClassifier(mouthhaarcascade)
print "Initialization completed in {0:.2f} seconds.\n".format(time.time() - initial_time)

#
# Main loop
#   Press "l" to learn a new image
#   Press "r" to reload image database
#   Press "v" to toggle voice synthesis
#   Press "b" for best guess of image
#   Press "e" to toggle eye detection
#   Press "p" to preprocess pictures using TanTriggs
#   Press <up/down arrow key> to increase/decrease detection threshold
#   Press <left/right arrow key> to increase/decrease number of images to use per subject
#   Press <esc> to quit

#
# Initialize and move windows
#
cv2.namedWindow('Identification Window')
cv2.moveWindow('Identification Window', 0,0)

#
# Here is where we'll place faces that we're seeing or learning (assumed to be 50x50)
# These are lined up along the bottom of the main picture window
#
cv2.namedWindow('Face - 0')
cv2.moveWindow('Face - 0', 0,500)
cv2.namedWindow('Face - 1')
cv2.moveWindow('Face - 1', 100,500)
cv2.namedWindow('Face - 2')
cv2.moveWindow('Face - 2', 200,500)
cv2.namedWindow('Face - 3')
cv2.moveWindow('Face - 3', 300,500)
cv2.namedWindow('Face - 4')
cv2.moveWindow('Face - 4', 400,500)
cv2.namedWindow('Face - 5')
cv2.moveWindow('Face - 5', 500,500)

#
# This is where we'll place faces that we've positively matched
# These are lined along the right side of the main picture window
#
cv2.namedWindow('Match - 0')
cv2.moveWindow('Match - 0', 640,0)
cv2.namedWindow('Match - 1')
cv2.moveWindow('Match - 1', 640,130)
cv2.namedWindow('Match - 2')
cv2.moveWindow('Match - 2', 640,260)
cv2.namedWindow('Match - 3')
cv2.moveWindow('Match - 3', 640,390)
cv2.namedWindow('Database - 0')
cv2.moveWindow('Database - 0', 740,0)
cv2.namedWindow('Database - 1')
cv2.moveWindow('Database - 1', 740,130)
cv2.namedWindow('Database - 2')
cv2.moveWindow('Database - 2', 740,260)
cv2.namedWindow('Database - 3')
cv2.moveWindow('Database - 3', 740,390)

lastpredicted_label = None

#
# The current_state changes, based on the current situation.   Most of these are triggered by keypresses at the bottom
#   State = "Loading"   --> This means we need to reload the image database and reload the model
#         = "Tracking"  --> This is the normal operation where we're just looking for faces
#         = "Learning"  --> This is the mode where are capturing images and saving them to the database
# 
current_state = "Loading"

#
# X is an empty list.   If it's blank after we come back from reading images, then we know we can't identify anything
# until we record some images.   A blank "X" triggers skipping most of the stuff except showing the original webcam image.
#
X = []

#
# The main loop:   The only way out of this is to press the "escape" key to exit the program.
#
while (1):
    #
    # If we need to load the images and generate the model, do it here
    #
    if (current_state == "Loading"):
        initial_time = time.time()
        print "Importing image database for: "
        [X,y,Z,subject_names] = read_images(pathdir)
        subject_list = list(y)

        print subject_names

        print "Import complete in {0:.2f} seconds.\n".format(time.time() - initial_time)

        #
        # If X is null, we didn't find any pictures.   If this is the case, don't bother trying to load
        # any model (or do face recognition later)
        #
        if X != []:
            #
            # The next two lines just create a dictionary of the names, as follows:
            #   [ 1, first_name in database]
            #   [ 2, second_name in database]
            #   ...
            #   [ n, last_name in database]
            #
            # This dictionary is used in for the greeting and labeling
            #
            list_of_labels = list(xrange(max(y)+1))
            subject_dictionary = dict(zip(list_of_labels, subject_names))
     
            #
            # This constructs the linear distriminant analysis matrix, which is used for facial identification
            #
            initial_time = time.time()
            print "Constructing linear discriminant analysis matrix for facial identification: "
            model.compute(Z,y)

            print "Construction completed in {0:.2f} seconds.\n".format(time.time() - initial_time)

        current_state = "Tracking"

    # 
    # Get a new frame from the webcam
    #
    rval, frame = vc.read()

    # 
    # Copy the frame adn convert the whole thing to black and white to make recognition easier
    #
    img = frame
    rows,cols,ch = frame.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #
    # Use the Haar Cascade to see if there are any faces in the picture
    # This is the bulk face detector, but it doesn't do any recognition of individuals at this point.
    #
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50, 50),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    
    #
    # For each face,
    #   1.  put a rectangle around it
    #   2.  A.  If we're in pre-learning mode, wait until we get a name
    #       B.  If we're in learning mode, save face and wait 1 second before starting again
    #       C.  If we're in identification mode, try to identify it
    #
    for (x,y,w,h) in faces:
        # 
        # Draw a blue box around the face that we've found
        #
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        #
        # Now, see if we can find the eyes, nose and mouth
        #
        detected_eyes = find_eyes(img, gray, [x,y,h,w])
        detected_noses = find_nose(img, gray, [x,y,h,w])
        detected_mouths = find_mouth(img, gray, [x,y,h,w])
        
        #
        # Resize the face to the same size as the database of faces
        #
        if len(detected_eyes) != 2 or len(detected_mouths) != 1:
            # 
            # We didn't get eyes or mouth for this picture, do a simple comparison
            #
            sampleImage = gray[y:y+h, x:x+w]
            #sampleImage = cv2.resize(sampleImage, (256,256)) & facefilter   <<<<----- Now filtering on input, not here
            sampleImage = cv2.resize(sampleImage, (256,256))
            #
            # If we're tracking eyes, since we never detected eyes or a mouth.... too much chance of a bad match
            # If we're not tracking details, go ahead and take a guess
            #
            if details_on:
                  continue
        else:
            #
            # Normalize picture by resizing and retilting, based on location of eyes and mouth
            # We're using a standard face model where the center of the left eye is at x,y = (30%, 45%)
            # the center of the right eye is at x,y = (70%, 45%) and the center of the mouth is x,y (50%, 85%)
            # This should realign any tilted or skewed faces into a simple normalized form.
            #
               
            centerleftx = detected_eyes[0][0]+detected_eyes[0][2]/2  # left side plus half width
            centerlefty = detected_eyes[0][1]+detected_eyes[0][3]/2  # top plus half height
            centerrightx = detected_eyes[1][0]+detected_eyes[1][2]/2  # left side plus half width
            centerrighty = detected_eyes[1][1]+detected_eyes[1][3]/2  # top plus half height
            centermouthx = detected_mouths[0][0]+detected_mouths[0][2]/2  # left size plus half width
            centermouthy = detected_mouths[0][1]+detected_mouths[0][3]/2  # top plus half height

            #
            # Warp picture to realign eyes and mouth where we want them to be
            # Eyes are at 30% from the left and right edges, 45% down from top of picture
            # Mouth is centered in middle, 85% of the way down the page
            #
            pts1 = np.float32([[centerleftx,centerlefty],[centerrightx,centerrighty],[centermouthx,centermouthy]])
            pts2 = np.float32([[cols*.3,rows*.45],[cols*.7,rows*.45],[cols*.50,rows*.85]])

            #
            # Affine tranformations take three points in the original picture and three points in the new picture.
            # Based on those three points, all other points can be mapped from the old picture to the new picture.
            # By choosing the center of the eyes and the middle of the mouth, this will have the effect of normalizing
            # the picture by leveling out the eyes and putting the center of the mouth back into the center of the picture.
            #
            M = cv2.getAffineTransform(pts1,pts2)
            warped_image = cv2.warpAffine(gray,M,(cols,rows))
                
            #
            # Now, all we have to do is resize the warped image into one we want to save
            # First, we mask the borders to try to eliminate lighting-effects that aren't on the face itself
            # This is just a black oval mask around the outside corners
            # 
            # sampleImage = cv2.resize(warped_image, (256, 256)) & facefilter  <<<----- Decided to filter on input
            sampleImage = cv2.resize(warped_image, (256, 256))

            # 
            # The display image is smaller (100x100) than the original picture
            # These are displayed in consecutive windows (from #0 to #5) according to the algorithm below
            display = cv2.resize(sampleImage, (100,100))
            cv2.imshow('Face - '+str(currentwindow), display)
            currentwindow = (currentwindow+1) % 6

            # 
            # If we're in a learning mode, capture the picture
            # pictures are kept in a directory structure indexed by name.
            # All of the pictures are timestamped to make them unique and saved under the subject's directory
            # This means if you reuse a name, it will just dump all the pictures into that directory.
            #
            if current_state == "Learning":
                print  pathdir+name+'/'+str(started_learning+current_saved)+'.jpg'
                cv2.imwrite( pathdir+name+'/'+str(started_learning+current_saved)+'.jpg', sampleImage);
                current_saved += 1
                time.sleep(1)
        #
        # Keep learning for 15 seconds or until we capture 6 images
        #
        if current_state == "Learning":
            if ((time.time() - started_learning) > 15) or (current_saved == 6):
                #
                # Stop learning if we've been learning for 15 seconds or saved 6 pictures
                #
                current_state = "Tracking"
            else:
                cv2.putText(frame,'Recorded '+str(current_saved)+' images for '+name, (x,y-3), cv2.FONT_HERSHEY_PLAIN,1,(0,0,250),1,1)
            # 
            # If we're learning, skip back to the top of the loop
            #
            continue

        #
        # If we don't have anything in the database, skip the recognition part
        #
        if X == []:
            break;  
          
        #
        # Do we recognize the current face?
        # The "predict" method will return the closest match of the current image to the database
        #
        finalimage = sampleImage & facefilter
        [ predicted_label, generic_classifier_output] = model.predict(finalimage)

        #
        # Determine if the prediction is within a certain "threshold".  This is actually the 
        # "distance" between the image and the database.   The closer the distance is to "0", the 
        # closer a match it really is.
        #
        # Higher thresholds result in less accuracy or more mis-identified pictures.
        #
        if int(generic_classifier_output['distances'][0]) > current_threshold * 4:
            high=current_threshold * 4
        else:
            high=int(generic_classifier_output['distances'][0])

        #
        # The percentage is calculated to tell us how close we are to a perfect match we have to the current image
        # This is an ARBITRARY calculation.   We could have done it anyway we wanted, but this seemed to work nicely 
        # 
        percentage = int((((current_threshold*4.0)-high)/(current_threshold*4.0))*100)

        if debug_on:
           print "Prediction:", subject_dictionary[predicted_label], str(percentage)+"%", generic_classifier_output['distances'][0]

        
        #
        # The percentage is high enough to call it a "match"
        #
        if percentage >= 80:
            cv2.putText(img,str(subject_dictionary[predicted_label])+"["+str(percentage)+"%]", (x,y-3), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),0,1)
            #
            # We definitively matched someone.
            # Give them a little vocalized greeting :-)
            #
            greet(subject_dictionary[predicted_label])
            #
            # If we have a new match, the picture alongside the first match in the database
            #
            if predicted_label != lastpredicted_label:
                display = cv2.resize(sampleImage, (100,100))
                cv2.imshow('Match - '+str(currentmatch), display)
                display = cv2.resize(X[subject_list.index(predicted_label)], (100,100))
                cv2.imshow('Database - '+str(currentmatch), display)
                currentmatch = (currentmatch+1) % 4
                lastpredicted_label = predicted_label
        #
        # The percentage is not high enough for a match, but close enough for a "maybe"
        #      
        elif percentage >= 70:
            cv2.putText(img,str(subject_dictionary[predicted_label])+"["+str(percentage)+"%]", (x,y-3), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),0,1)
        #
        # The percentage is not high enough for a maybe, but close enough for a "it kinda looks like him/her"
        # 
        elif percentage > 60:
            cv2.putText(img,str(subject_dictionary[predicted_label])+"["+str(percentage)+"%]", (x,y-3), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),0,1)
        #
        # The percentage is not high enough for anything, but we've been asked to 'take our best guess'
        # 
        elif bestguess_on:
            cv2.putText(img,str(subject_dictionary[predicted_label])+"["+str(percentage)+"%]", (x,y-3), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),0,1)
          
    #
    # Print the control information
    # Note that the 'd' command (for debugging) doesn't appear on the screen
    #
    cv2.putText(img, "Identification Threshold: ", (390,20), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    cv2.putText(img, str(current_threshold), (600,20), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,1)
    cv2.putText(img, "Speech Synthesis (v): ", (413,40), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    cv2.putText(img, onoff[voice_on], (600,40), cv2.FONT_HERSHEY_PLAIN,1,(0, 255,0),0,1)
    cv2.putText(img, "Eye Tracking (e): ", (450,60), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    cv2.putText(img, onoff[details_on], (600,60), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,1)
    cv2.putText(img, "Best Guess (b): ", (465,80), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    cv2.putText(img, onoff[bestguess_on], (600,80), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,1)
    cv2.putText(img, "Preprocess (p): ", (465,100), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    cv2.putText(img, onoff[preprocess_on], (600,100), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,1)

    #
    # Legend at the bottom
    #
    cv2.putText(img, "Learn (l):     Recompute LDA matrix (r):    Quit (<ESC>)   Subjects("+str(current_max_subjects)+")", (10,470), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)

    #
    # Print list of recently seen people
    #
    cv2.putText(img, "Recently seen: ", (10,20), cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),0,1)
    current_time = time.time()
    count = 0
    for person in greetingdict:
        if current_time - greetingdict[person] > GREETINGREPEAT:
            #
            # Person has been in database too long, remove them
            #
            del greetingdict[person]
            #
            # Since we changed the dictionary we're iterating on, STEP SINCE THIS IS A BIG PYTHON NO-NO.
            # We'll remove older entries the next time around
            #
            break
        else:
            count += 1
            cv2.putText(img, person, (10,20+count*20), cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),0,1)

    #
    # Finally, after all of this, go ahead and show the image in the window
    #
    cv2.imshow('Identification Window',img)

    #
    # Now, wait for a key (but only for 10 ms).  If we don't get a key, just start the loop over
    # If we get a key, act on that key
    #
    key = cv2.waitKey(10)

    #print "Key value:", key
    if key  == 27:  # the <ESC> key
        #
        # End the program
        break
    elif key == ord('l'):
        #
        # Go get the new images, but don't load them yet since we might be learning more people
        #
        current_state = "Learning"
        current_saved = 0
        name = raw_input("Subject's name?: ")
        if not os.path.exists(pathdir+name): 
            os.makedirs(pathdir+name)
        started_learning = time.time()
    elif key == ord('r'):
        #
        # Tell the loop to re-load the database with the new images
        #
        current_state = "Loading"
    elif key == 2490368:    # Up arrow
        current_threshold += 10
    elif key == 2621440:    # Down arrow
        current_threshold -= 10
        if current_threshold < 10:
            current_threshold = 10;
    elif key == 2424832:     # Left arrow
        current_max_subjects -= 1
        if current_max_subjects < 1:
            current_max_subjects = 1
    elif key == 2555904:     # Right arrow
        current_max_subjects += 1
    elif key == ord('e'):
        details_on = not details_on
    elif key == ord('v'):
        voice_on = not voice_on
    elif key == ord('b'):
        bestguess_on = not bestguess_on
    elif key == ord('d'):
        debug_on = not debug_on
    elif key == ord('p'):
        preprocess_on = not preprocess_on
        if not preprocess_on:
            # This doesn't use any preprocessing of images TanTriggsPreprocessing
            current_threshold = IDENTIFIED_THRESHOLD
            model = PredictableModel(Fisherfaces(), NearestNeighbor())
        else:
            # This uses TanTriggsPreprocessing to account for lighting differences
            # This is "on" by default
            # This is likely to get better guesses, so we narrow down the threshold
            # to prevent mis-identifying
            current_threshold = IDENTIFIED_THRESHOLD/TANTRIGGS_SCALER
            feature = ChainOperator(TanTriggsPreprocessing(), Fisherfaces())
            model = PredictableModel(feature, NearestNeighbor())
        current_state = "Loading"

cv2.destroyAllWindows()
vc.release()
