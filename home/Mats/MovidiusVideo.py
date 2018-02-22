#! /usr/bin/env python3

# Example script based on the caffe model GoogleNet example from Intel, but changed to use an OpenCV videostream as input
# showing the input image and the image passed to the Movidius compute stick
# Please note that this script can't be executed from within MRL because it uses python3 ( not jython as MRL uses )

from imutils.video import FPS

from mvnc import mvncapi as mvnc
import sys
import numpy
import cv2
import time
import csv
import os
import sys

dim=(224,224)
EXAMPLES_BASE_DIR='../../'

# ***************************************************************
# get labels
# ***************************************************************
labels_file=EXAMPLES_BASE_DIR+'data/ilsvrc12/synset_words.txt'
labels=numpy.loadtxt(labels_file,str,delimiter='\t')

# ***************************************************************
# configure the NCS
# ***************************************************************
mvnc.SetGlobalOption(mvnc.GlobalOption.LOG_LEVEL, 2)

# ***************************************************************
# Get a list of ALL the sticks that are plugged in
# ***************************************************************
devices = mvnc.EnumerateDevices()
if len(devices) == 0:
	print('No devices found')
	quit()

# ***************************************************************
# Pick the first stick to run the network
# ***************************************************************
device = mvnc.Device(devices[0])

# ***************************************************************
# Open the NCS
# ***************************************************************
device.OpenDevice()

network_blob='graph'

#Load blob
with open(network_blob, mode='rb') as f:
	blob = f.read()

graph = device.AllocateGraph(blob)
graph.SetGraphOption(mvnc.GraphOption.DONT_BLOCK, 1)

# ***************************************************************
# Load the image
# ***************************************************************
ilsvrc_mean = numpy.load(EXAMPLES_BASE_DIR+'data/ilsvrc12/ilsvrc_2012_mean.npy').mean(1).mean(1) #loading the mean file
cap = cv2.VideoCapture(0)
fps = FPS().start()
# img = cv2.imread(EXAMPLES_BASE_DIR+'data/images/nps_electric_guitar.png')

def processImage():
  global cap
  ret, orgimg = cap.read()
  #
  img=cv2.resize(orgimg,dim)
  img = img.astype(numpy.float32)
  img[:,:,0] = (img[:,:,0] - ilsvrc_mean[0])
  img[:,:,1] = (img[:,:,1] - ilsvrc_mean[1])
  img[:,:,2] = (img[:,:,2] - ilsvrc_mean[2])

  # ***************************************************************
  # Send the image to the NCS
  # ***************************************************************
  if(graph.LoadTensor(img.astype(numpy.float16), 'user object')):
    # ***************************************************************
    # Get the result from the NCS
    # ***************************************************************
    output, userobj = graph.GetResult()
    # ***************************************************************
    # Print the results of the inference form the NCS
    # ***************************************************************
    order = output.argsort()[::-1][:6]
##  print('\n------- predictions --------')
##  for i in range(0,5):
##  	print ('prediction ' + str(i) + ' (probability ' + str(output[order[i]]) + ') is ' + labels[order[i]] + '  label index is: ' + str(order[i]) )
    cv2.putText(orgimg, labels[order[0]],
		(10, orgimg.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 255), 1)
  else:
    print("Waited")
  # End of if statement
  cv2.imshow("Camera",orgimg)  
  cv2.imshow("Resized",img)
  
  fps.update()

while(True):
  processImage()
  if cv2.waitKey(1) &0xFF == ord('q'):
      break
 
 # ***************************************************************
# Clean up the graph and the device
# ***************************************************************
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
#
graph.DeallocateGraph()
device.CloseDevice()
cap.release()
cv2.destroyAllWindows()  


