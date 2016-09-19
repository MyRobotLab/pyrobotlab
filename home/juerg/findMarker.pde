import kinect4WinSDK.*;
import kinect4WinSDK.SkeletonData;

import jp.nyatla.nyar4psg.*;
import jp.nyatla.nyar4psg.utils.*;

import java.net.URL;

Kinect kinect;
ArrayList <SkeletonData> bodies;

String camParams = "D:/Projekte/Processing/Kinect/camera_para.dat";
String pattern = "D:/Projekte/Processing/Kinect/patt.hiro";

String urlSpeak = "http://10.1.1.20:8888/api/services/i01.mouth/speakBlocking/%22";
String terminator = "%22";

String urlExec = "http://10.1.1.20:8888/api/services/python/exec/";

int arWidth = 640;
int arheight = 480;
int numMarkers = 1;
int centerRange = 50;
int size60 = 80;
float sizeRange = 0.05;
float heightRange = 1.05;
int todo;

String lastCommand;

public class Marker {
  int x;
  int y;
  int height;
  int width;
  int heightLeft;
  int heightRight;
  }
void Marker() {
}

Marker markerData = new Marker();

MultiMarker nya;
PImage cam;
//PImage depht;

URL command;



String right1 = "please move base to the right";
String right2 = "move further right please";

String left1 = "please move base to the left";
String left2 = "move further left please";

String forward1 = "please move base closer to the door";
String forward2 = "closer please";

String backward1 = "please move base away from the door";
String backward2 = "further away please";

String rotLeft1 = "please rotate base to the left";
String rotLeft2 = "rotate further left please";

String rotRight1 = "please rotate base to the right";
String rotRight2 = "rotate further right please";

String wrongLeft = "good boy, left is where your thumb is on the right side";
String wrongRight = "good boy, right is where your thumb is on the left side";

String done = "Thanks a lot, I think it's the position where I wanted to be";

String noMarkerFound = "Unfortunately I can not find the marker in the image";

void setup()
{
  size (640, 480, P3D);

 // create a text font for the coordinates and numbers on the boxes at a decent (80) resolution
  textFont(createFont("Arial", 80));
  
  // load the input image and create a copy at the resolution of the AR detection (otherwise nya.detect will throw an assertion error!)
  kinect = new Kinect(this);
  
  // create a new MultiMarker at a specific resolution (arWidth x arheight), with the default camera calibration and coordinate system
  nya = new MultiMarker(this, arWidth, arheight, camParams, NyAR4PsgConfig.CONFIG_PSG);
  nya.addARMarker(pattern, 80);

  // set the delay after which a lost marker is no longer displayed. by default set to something higher, but here manually set to immediate.
  nya.setLostDelay(1);
  
  smooth();
}

void draw()
{
  background(0);
  cam = kinect.GetImage();
  //depht = kinect.GetDepth();
  image(cam, 0, 0);
  nya.detect(cam);
  if (!nya.isExist(0)) {
    if (lastCommand == noMarkerFound) {
      return;
    }
    sendCommand(noMarkerFound, 0);
    lastCommand = noMarkerFound;
    return;
  }
  markerData=drawMarker();
  commandBot(markerData);
  pause(100);
  }

void pause(int ms) {
  try {
    Thread.sleep(ms);
  } catch(InterruptedException ex) {
    Thread.currentThread().interrupt();
  }
}

void commandBot(Marker marker) {
  println("marker x,y,heightLeft: ", marker.x, marker.y, marker.height, marker.width, marker.heightLeft, marker.heightRight);
  
  //////////////////////////////////////////////////////////
  // try to move marker into centered x position by rotation
  //////////////////////////////////////////////////////////
  if (marker.x < width/2 - centerRange) {
    if (lastCommand == rotRight1) {
      sendCommand(rotRight2, 0);
      return;
    } else {
      sendCommand(rotRight1, 1);
      lastCommand = rotRight1;
      return;
    }
  }  
  if (marker.x > width/2 + centerRange) {
    if (lastCommand == rotLeft1) {
      sendCommand(rotLeft2, 0);
      return;
    } else {
      sendCommand(rotLeft1, 2);
      lastCommand = rotLeft1;
      return;
    }
  }
  
  //////////////////////////////////////////////////////////
  // try to move into front of marker (might trigger rotate again)
  //////////////////////////////////////////////////////////
  if (marker.width < int(marker.height * heightRange)) {
    if (marker.heightLeft < marker.heightRight - 2) {
      if (lastCommand == right1) {
        sendCommand(right2, 0);
        return;
      } else {
        sendCommand(right1, 3);
        lastCommand = right1;
        return;
      }
    }
    
    if (marker.heightLeft > marker.heightRight + 2) {
      if (lastCommand == left1) {
        sendCommand(left2, 0);
        return;
      } else {
        sendCommand(left1, 4);
        lastCommand = left1;
        return;
      }
    }
  }
  
  //////////////////////////////////////////////////////////
  // try to move into good distance from the marker
  //////////////////////////////////////////////////////////
  if (marker.heightLeft < int(size60 * (1-sizeRange))) {
    if (lastCommand == forward1) {
      sendCommand(forward2, 0);
      return;
    } else {
      sendCommand(forward1, 5);
      lastCommand = forward1;
      return;
    }
  } 
  if (marker.heightLeft > int(size60 * (1 + sizeRange))) {
    if (lastCommand == backward1) {
      sendCommand(backward2, 0);
      return;
    } else {
      sendCommand(backward1, 6);
      lastCommand = backward1;
      return;
    }
  }
  if (lastCommand != done) {
    sendCommand(done,0);
    lastCommand=done;
  }
}

void sendCommand(String text, int todo) {
  String command = urlSpeak + text.replace(" ", "%20") + terminator;
  println(text);
  println(command);
  try {
  new URL(command).openStream().close();
  } catch (IOException e) {}
  
  switch (todo) {
    case 1: 
      command = urlExec + "rotateMeRight()";
      break;
    case 2: 
      command = urlExec + "rotateMeLeft()";
      break;
    case 3: 
      command = urlExec + "moveMeLeft()";
      break;
    case 4: 
      command = urlExec + "moveMeLeft()";
      break;
//    case 5: 
//      command = urlExec + "moveMeForward()";
//      break;
//    case 6:
//      command = urlExec + "moveMeBackward()";
//      break;
    default:
      command = "";
  }

  if (command != "") {
    try {
    new URL(command).openStream().close();
    } catch (IOException e) {}
  }
    
  
}

// this function draws the marker coordinates, note that this is completely 2D and based on the AR dimensions (not the final display size)
Marker drawMarker() {

  Marker sum = new Marker();
  Marker marker = new Marker();
  
  // set the text alignment (to the left) and size (small)
  textAlign(LEFT, TOP);
  textSize(10);
  noStroke();
  // scale from AR detection size to sketch display size (changes the display of the coordinates, not the values)
  //scale(displayScale);
  // for all the markers...
  //depht.loadPixels();

  // if the marker does NOT exist (the ! exlamation mark negates it) continue to the next marker, aka do nothing
  if ((nya.isExist(0))) {

  // the following code is only reached and run if the marker DOES EXIST
  // get the four marker coordinates into an array of 2D PVectors
  PVector[] pos2d = nya.getMarkerVertex2D(0);
  // draw each vector both textually and with a red dot
  for (int j=0; j<pos2d.length; j++) {
    String s = "(" + int(pos2d[j].x) + "," + int(pos2d[j].y) + ")";
    fill(255);
    // error rect(pos2d[j].x, pos2d[j].y, textWidth(s) + 3, textAscent() + textDescent() + 3);
    fill(0);
    text(s, pos2d[j].x + 2, pos2d[j].y + 2);
    fill(255, 0, 0);
    ellipse(pos2d[j].x, pos2d[j].y, 5, 5);
    
    // sum up x and y positions
    sum.x += pos2d[j].x;
    sum.y += pos2d[j].y;
  }

  // build the marker data, corner index is 0 1
  //                                        3 2
  marker.height = int((pos2d[3].y + pos2d[2].y - pos2d[0].y - pos2d[1].y) / 2);
  marker.width = int((pos2d[1].x + pos2d[2].x - pos2d[0].x - pos2d[3].x) / 2);
  marker.heightLeft = int(pos2d[3].y - pos2d[0].y);
  marker.heightRight = int(pos2d[2].y - pos2d[1].y);  
  }

  marker.x = sum.x/4;
  marker.y = sum.y/4;
 
  return marker;
}


void appearEvent(SkeletonData _s) 
{
//  if (_s.trackingState == Kinect.NUI_SKELETON_NOT_TRACKED) 
//  {
//    return;
//  }
//  synchronized(bodies) {
//    bodies.add(_s);
//  }
}

void disappearEvent(SkeletonData _s) 
{
//  synchronized(bodies) {
//    for (int i=bodies.size ()-1; i>=0; i--) 
//    {
//      if (_s.dwTrackingID == bodies.get(i).dwTrackingID) 
//      {
//        bodies.remove(i);
//      }
//    }
//  }
}

void moveEvent(SkeletonData _b, SkeletonData _a) 
{
//  if (_a.trackingState == Kinect.NUI_SKELETON_NOT_TRACKED) 
//  {
//    return;
//  }
//  synchronized(bodies) {
//    for (int i=bodies.size ()-1; i>=0; i--) 
//    {
//      if (_b.dwTrackingID == bodies.get(i).dwTrackingID) 
//      {
//        bodies.get(i).copy(_a);
//        break;
//      }
//    }
//  }
}