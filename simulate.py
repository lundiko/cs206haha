#petra waterstreet
from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()

#import constants as c
#import pyrosim.pyrosim as pyrosim
#import pybullet as p
#import numpy
#import pybullet_data
#import time
#import random
#amplitudeBack = -(c.AMPLITUDE)
#frequencyBack  = -(c.FREQUENCY)
#phaseOffsetBack  = 0

#amplitudeFront = c.AMPLITUDE
#frequencyFront = c.FREQUENCY
#phaseOffsetFront = c.PHASEOFFSETFRONT

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#physics forces
#p.setGravity(0,0,c.GRAVITY)
#planeId = p.loadURDF("plane.urdf")
#the box
#robotId = (p.loadURDF("body.urdf"))
#p.loadSDF("world.sdf")
#Pyrosim has to do some additional setting up when it is used to simulate sensors. 
#
#robotId contains an integer, indicating which robot you want prepared for simulation. 


#targetAnglesFront = numpy.zeros(c.ANGLEVALUES)
#targetAnglesBack = numpy.zeros(c.ANGLEVALUES)
#x = numpy.linspace((0), (2*numpy.pi), 1000)
#count = 0

#for j in x:
#    targetAnglesFront[count] = amplitudeFront * numpy.sin(frequencyFront * j +phaseOffsetFront)
#    targetAnglesBack[count] = amplitudeBack * numpy.sin(frequencyBack * j +phaseOffsetBack)
#    count +=1


#for i in range(c.ANGLEVALUES):
#    time.sleep(0.016)
#    p.stepSimulation()
    #touch sensor
#    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #BACK
#    pyrosim.Set_Motor_For_Joint(
#        bodyIndex = robotId,
#        #had the KeyError problem
#        jointName = "Torso_BackLeg",
#        controlMode = p.POSITION_CONTROL,
#        targetPosition = targetAnglesBack[i],
#        maxForce = c.FORCE)
    #FRONT
#    pyrosim.Set_Motor_For_Joint(
#        bodyIndex = robotId,
#        #had the KeyError problem
#        jointName = "Torso_FrontLeg",
#        controlMode = p.POSITION_CONTROL,
#        targetPosition = targetAnglesFront[i],
#        maxForce = c.FORCE)

