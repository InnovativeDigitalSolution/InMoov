def negative():
  i01.setHandSpeed("left", 31.0, 31.0, 31.0, 31.0, 31.0, 31.0)
  i01.setHandSpeed("right", 26.00, 26.00, 26.00, 26.00, 26.00, 100.0)
  i01.setArmSpeed("right", 43.0, 22.0, 22.0, 22.0)
  i01.moveHead(18,75)
  sleep(1)
  i01.moveHead(120,75)
  sleep(1)
  i01.moveHead(18,75)
  i01.moveArm("left",66,52,59,23)
  i01.moveArm("right",59,60,50,16)
  i01.moveHand("left",140,148,140,10,10,0)
  i01.moveHand("right",140,148,140,10,10,0)
  sleep(2)
  relax()

