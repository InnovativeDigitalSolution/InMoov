def armsUp():
  inMoov.startedGesture()
  inMoov.setHeadVelocity(-1,-1)
  inMoov.moveHead(180,86)
  sleep(1)
  inMoov.setHandVelocity("left",50,50,50,50,50,-1)
  inMoov.setHandVelocity("right",50,50,50,50,50,-1)
  inMoov.moveHand("left",170,170,170,170,170,33)
  inMoov.moveHand("right",170,170,170,170,170,180)
  sleep(3)
  inMoov.setArmVelocity("left",-1.0,-1.0,-1.0,-1.0)
  inMoov.setArmVelocity("right",-1.0,-1.0,-1.0,-1.0)
  inMoov.setTorsoVelocity(-1.0,-1.0,-1.0)
  inMoov.moveArm("left",90,90,170,20)
  inMoov.moveArm("right",90,90,173,20)
  sleep(9)
  inMoov.setHandVelocity("left",-1,-1,-1,-1,-1,-1)
  inMoov.setHandVelocity("right",-1,-1,-1,-1,-1,-1)
  inMoov.moveHead(180,86)
  inMoov.moveArm("left",5,90,170,10)
  inMoov.moveArm("right",5,90,173,10)
  inMoov.moveHand("left",2,2,2,2,2,33)
  inMoov.moveHand("right",2,2,2,2,2,180)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  inMoov.finishedGesture()
