def releaseleftclothes():
  i01.startedGesture()
  ##arms get to middle
  i01.setHandSpeed("left", 100.0, 36, 36, 36, 100.0, 36)
  i01.setHandSpeed("right", 100.0, 26.00, 26.00, 100.0, 100.0, 36)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(50, 36)
  i01.setTorsoSpeed(100.0,36,100.0)
  i01.moveHead(0,80,82,0,65)
  i01.moveArm("left",97,51,25,27)
  i01.moveArm("right",81,52,22,18)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",180,180,180,180,180,180)
  i01.moveTorso(90,90,90)

  sleep(4)
  ##arms spread
  i01.setHandSpeed("left", 100.0, 36, 36, 36, 100.0, 36)
  i01.setHandSpeed("right", 100.0, 100.0, 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(50, 36)
  i01.setTorsoSpeed(100.0,36,100.0)
  
  sleep(2)
  i01.moveHead(90,90,82,78,65)
  i01.moveArm("left",97,51,25,22)
  i01.moveArm("right",90,135,22,36)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",180,180,180,180,180,139)
  i01.moveTorso(64,80,90)
  sleep(2)
  ##release clothes
  i01.setHandSpeed("left", 100.0, 36, 36, 36, 100.0, 36)
  i01.setHandSpeed("right",  100.0, 36, 36, 36, 36, 36)
  i01.setArmSpeed("left", 100.0, 100.0, 100.0, 100.0)
  i01.setArmSpeed("right", 100.0, 100.0, 100.0, 100.0)
  i01.setHeadSpeed(50, 36)
  i01.setTorsoSpeed(100.0,36,100.0)
  i01.moveHead(38,43,51,10,65)
  i01.moveArm("left",97,51,25,22)
  i01.moveArm("right",90,135,22,36)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",0,0,0,0,0,139)
  i01.moveTorso(66,80,90)
  sleep(4)
  ##Relax
  i01.moveHead(80,86,82,78,65)
  i01.moveArm("left",5,84,28,14)
  i01.moveArm("right",5,82,28,16)
  i01.moveHand("left",92,33,37,71,66,25)
  i01.moveHand("right",81,66,82,60,105,113)
  i01.moveTorso(95,90,90)
  sleep(1)
  i01.finishedGesture()
