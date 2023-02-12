#petra waterstreet
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import pybullet_data
import time
import random
amplitudeBack = -numpy.pi/8
frequencyBack  = -8
phaseOffsetBack  = 0

amplitudeFront = numpy.pi/8
frequencyFront = 8
phaseOffsetFront = numpy.pi/4 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#physics forces
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#the box
robotId = (p.loadURDF("body.urdf"))
p.loadSDF("world.sdf")
#Pyrosim has to do some additional setting up when it is used to simulate sensors. 
pyrosim.Prepare_To_Simulate(robotId)
#robotId contains an integer, indicating which robot you want prepared for simulation. 
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)
targetAnglesFront = numpy.zeros(1000)
targetAnglesBack = numpy.zeros(1000)
x = numpy.linspace((0), (2*numpy.pi), 1000)
count = 0

for j in x:
    targetAnglesFront[count] = amplitudeFront * numpy.sin(frequencyFront * j +phaseOffsetFront)
    targetAnglesBack[count] = amplitudeBack * numpy.sin(frequencyBack * j +phaseOffsetBack)
    count +=1


for i in range(1000):
    time.sleep(0.016)
    p.stepSimulation()
    #touch sensor
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #BACK
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        #had the KeyError problem
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBack[i],
        maxForce = 500)
    #FRONT
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        #had the KeyError problem
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFront[i],
        maxForce = 500)
#file save
with open('data/backData.npy', 'wb') as f:
    numpy.save(f,backLegSensorValues)
    f.close
with open('data/frontData.npy', 'wb') as f:
    numpy.save(f,frontLegSensorValues)
    f.close
p.disconnect()
print(backLegSensorValues)
