# ##############################################################################
#            *** LEFT ARM ***
# ##############################################################################

  
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isLeftArmActivated=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  isLeftArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftArmActivated') 

except:
  errorSpokenFunc('ConfigParserProblem','leftarm.config')
  pass
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isLeftArmActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full" ) or ScriptType=="Virtual":
  isLeftArmActivated=1
  if LeftPortIsConnected==True:

    leftArm = Runtime.create("i01.leftArm", "InMoovArm")
    leftArm.startPeers()
    #pffff :) we need to manualy load now to get last position to avoid breaking parts
    leftArm.bicep.load()
    leftArm.shoulder.load()
    leftArm.rotate.load()
    leftArm.omoplate.load()
    #end pffff :)
    try:      
      leftArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'bicep')) 
      leftArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'shoulder')) 
      leftArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rotate')) 
      leftArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'omoplate')) 
      
      leftArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'bicep'))
      leftArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'shoulder'))
      leftArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rotate'))
      leftArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'omoplate'))
    except:
      errorSpokenFunc('ConfigParserProblem',ThisSkeletonPart)
      pass
      
    leftArm.bicep.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'))
    leftArm.shoulder.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'))
    leftArm.rotate.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'))
    leftArm.omoplate.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'))
    
    i01.startLeftArm(MyLeftPort,BoardTypeMyLeftPort)
    
    leftArm.rest()
            
    leftArm.bicep.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'bicep'))
    leftArm.shoulder.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'shoulder'))
    leftArm.rotate.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rotate'))
    leftArm.omoplate.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'omoplate'))

  else:
    #we force parameter if arduino is off
    isLeftArmActivated=0