def presentation():
  i01.startedGesture()
  i01.setArmVelocity("right", 3, 3, 5.0, 5.0);
  i01.setArmVelocity("left", 3, 3, 5.0, 5.0);
  i01.setHeadVelocity(5.0,5.0)
  i01.moveArm("right", 64, 94, 10, 10);
  i01.mouth.speakBlocking("Hello, my name is Harry.  I am the first life size humanoid robot you can 3D print and animate")
  i01.moveHead(65,66)
  i01.moveArm("left", 64, 104, 10, 11);
  i01.moveArm("right", 44, 84, 10, 11);
  i01.mouth.speakBlocking("I was built by Kevin Waters.")
  i01.moveHead(75,86)
  i01.moveArm("left", 54, 104, 10, 11);
  i01.moveArm("right", 64, 84, 10, 20);
  i01.mouth.speakBlocking("I was printed out on a 3D printer.")
  i01.moveHead(65,96)
  i01.moveArm("left", 44, 94, 10, 20);
  i01.moveArm("right", 54, 94, 20, 11);
  i01.mouth.speakBlocking("My parts were design by Gael Langevin.  He is a sculptor and model maker from Paris.")

  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("My brain is powered by My Robot Lab.  It is an open source java application for creative machine control.")
  i01.moveHead(65,86)
  i01.moveArm("left", 24, 94, 10, 11);
  i01.moveArm("right", 24, 94, 10, 11);
  i01.mouth.speakBlocking("My software runs on 2 arduinos and a raspberry pi.")
  i01.moveHead(85,86)
  i01.moveArm("left", 5, 94, 20, 30);
  i01.moveArm("right", 24, 124, 10, 20);
  i01.mouth.speakBlocking("I have 2 cameras in my head that allow me to see and 25 servo motors that allow me to move.")
  i01.moveHead(75,96)
  i01.moveArm("left", 24, 104, 10, 11);
  i01.moveArm("right", 5, 94, 20, 30);
  i01.mouth.speakBlocking("I have a microphone so you can talk to me and as you may have noticed, I can speak also!")
  i01.moveHead(75,96)
  i01.moveArm("left", 5, 94, 10, 11)
  i01.moveArm("right", 4, 94, 10, 11);
  i01.mouth.speakBlocking("My brain is powered by A I M L.  Artificial Intellegence Markup Language.")
  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("I am able to rememeber what I see and hear.  These memories are stored in a Solr index.")

  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("I can use these memories to build and train neural networks so that I can recognize new objects.")

  i01.moveHead(75,86)
  i01.moveArm("left", 54, 104, 10, 11);
  i01.moveArm("right", 64, 84, 10, 20);
  i01.mouth.speakBlocking("When I don't know the answer to a question, I can call out to a natural language understanding api that was developed at K M W Technologies.")


  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("I can use these memories to build and train neural networks so that I can recognize new objects.")

  i01.moveHead(75,76)
  i01.moveArm("left", 64, 94, 20, 11);
  i01.moveArm("right", 34, 94, 10, 11);
  i01.mouth.speakBlocking("I enjoy interacting with humans.")

  i01.moveHead(65,96)
  i01.moveArm("left", 44, 94, 10, 20);
  i01.moveArm("right", 54, 94, 20, 11);
  i01.mouth.speakBlocking("When I am not running autonomously, I can be remotely controlled.")

  i01.moveHead(65,66)
  i01.moveArm("left", 64, 104, 10, 11);
  i01.moveArm("right", 44, 84, 10, 11);
  i01.mouth.speakBlocking("If you want you can attach to the video streams in my head and view them in a virtual reality head set like the Oculus Rift.")


  sleep(1)
  i01.finishedGesture()

  relax()
  fullspeed()

