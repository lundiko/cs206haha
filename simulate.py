#petra waterstreet
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import pybullet_data
import time
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
for i in range(1001):
    time.sleep(0.016)
    p.stepSimulation()
    #touch sensor
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = 0.0,
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
