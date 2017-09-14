public OpenCVData setOpenCVData(OpenCVData data) {

    switch (state) {

      case STATE_FACE_DETECT:
        // check for bounding boxes
        // data.setSelectedFilterName(FaceDetectFilterName);
        ArrayList<Rectangle> bb = data.getBoundingBoxArray();

        if (bb != null && bb.size() > 0) {

          // data.logKeySet();
          // log.error("{}",bb.size());

          // found face
          // find centroid of first bounding box
          lastPoint.x = bb.get(0).x + bb.get(0).width / 2;
          lastPoint.y = bb.get(0).y + bb.get(0).height / 2;
          updateTrackingPoint(lastPoint);

          ++faceFoundFrameCount;

          // dead zone and state shift
          if (faceFoundFrameCount > faceFoundFrameCountMin) {
            // TODO # of frames for verification
            invoke("foundFace", data);
            // data.saveToDirectory("data");
          }

        } else {
          // lost track

          faceFoundFrameCount = 0;

          if (scan) {
            TrackingServoData x = servoControls.get("x");
            TrackingServoData y = servoControls.get("y");
            double xpos = x.servoControl.getPos();
            double ypos = y.servoControl.getPos();

            if (xpos + x.scanStep >= x.servoControl.getMaxInput() && x.scanStep > 0 || xpos + x.scanStep <= x.servoControl.getMinInput() && x.scanStep < 0) {
              x.scanStep *= -1;
              
              //Acapulco Rolf
              //14/09/2017
              //remove "y" Math.random() logic              
              //double newY = y.servoControl.getMinInput() + (Math.random() * (y.servoControl.getMaxInput() - y.servoControl.getMinInput()));
              //y.servoControl.moveTo(newY);
            }
            
            //Acapulco Rolf
            //14/09/2017
            //add y position logic identical to  position logic
            if (ypos + y.scanStep >= y.servoControl.getMaxInput() && y.scanStep > 0 || ypos + y.scanStep <= y.servoControl.getMinInput() && y.scanStep < 0) {
                y.scanStep *= -1;
                
                //Acapulco Rolf
                //14/09/2017
                //double newY = y.servoControl.getMinInput() + (Math.random() * (y.servoControl.getMaxInput() - y.servoControl.getMinInput()));
                //y.servoControl.moveTo(newY);
              }
            

            x.servoControl.moveTo(xpos + x.scanStep);
            
            //Acapulco Rolf
            //14/09/2017
            y.servoControl.moveTo(ypos + y.scanStep);
            
          }
          // state = STATE_FACE_DETECT_LOST_TRACK;
        }

        // if scanning stop scanning

        // if bounding boxes & no current tracking points
        // set set of tracking points in square - search for eyes?
        // find average point ?
        break;

      case STATE_IDLE:
        // setForegroundBackgroundFilter(); FIXME - setFGBGFilters for
        // different detection
        break;

      case STATE_LK_TRACKING_POINT:
        // extract tracking info
        // data.setSelectedFilterName(LKOpticalTrackFilterName);
        Point2Df targetPoint = data.getFirstPoint();
        if (targetPoint != null) {
          updateTrackingPoint(targetPoint);
        }
        break;

      case STATE_LEARNING_BACKGROUND:
        waitInterval = 3000;
        waitForObjects(data);
        break;

      case STATE_SEARCHING_FOREGROUND:
        waitInterval = 3000;
        waitForObjects(data);
        break;

      default:
        error("recieved opencv data but unknown state");
        break;
    }

    return data;
  }
