#petra waterstreet
import pyrosim.pyrosim as pyrosim
import pybullet as p
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
for x in range(1001):
    time.sleep(0.016)
    p.stepSimulation()
    #touch sensor
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)
p.disconnect()
