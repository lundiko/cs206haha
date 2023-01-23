import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for x in range(1001):
    time.sleep(0.016)
    p.stepSimulation()
    print(x)
p.disconnect()
