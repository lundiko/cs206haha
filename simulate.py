#petra waterstreet
import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#physics forces
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
#the box
p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for x in range(1001):
    time.sleep(0.016)
    p.stepSimulation()
    print(x)
p.disconnect()
