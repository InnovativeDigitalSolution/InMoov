def brake():
  #neopixel.write(9)
  i01.startedGesture()
  i01.moveHead(80,86)
  i01.moveArm("left",5,90,30,10)
  i01.moveArm("right",5,90,30,10)
  i01.moveHand("left",45,40,30,25,35,90)
  i01.moveHand("right",55,2,50,48,30,90)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.moveHead(20,86)
  i01.moveArm("left",21,92,49,22)
  i01.moveArm("right",38,91,43,10)
  i01.moveHand("left",45,40,30,25,35,90)
  i01.moveHand("right",89,127,123,48,30,90)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.moveHead(20,106)
  i01.moveArm("left",75,69,49,22)
  i01.moveArm("right",38,91,43,10)
  i01.moveHand("left",120,80,74,106,35,90)
  i01.moveHand("right",89,127,123,48,30,90)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.moveHead(20,93)
  i01.moveArm("left",75,69,49,22)
  i01.moveArm("right",71,66,60,10)
  i01.moveHand("left",120,80,74,106,35,90)
  i01.moveHand("right",89,127,123,48,30,146)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.moveHead(110,93)
  i01.moveArm("left",75,69,49,22)
  i01.moveArm("right",71,66,60,10)
  i01.moveHand("left",120,80,74,106,35,90)
  i01.moveHand("right",89,127,123,48,30,146)
  i01.moveTorso(90,90,90)
  sleep(3)
  i01.mouth.speakBlocking("Should I brake that")
  #i01.mouth.speakBlocking(u"Должен ли я тормозить")
  i01.moveHead(110,93)
  i01.moveArm("left",90,69,84,22)
  i01.moveArm("right",71,66,60,10)
  i01.moveHand("left",138,134,168,168,120,90)
  i01.moveHand("right",124,142,151,48,30,146)
  i01.moveTorso(90,90,90)
  i01.finishedGesture()

