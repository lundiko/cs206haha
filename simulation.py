import constants as c
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import time
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.GRAVITY)
        self.world = WORLD()
        self.robot = ROBOT()
        #self.sensor = SENSOR()
        #self.motor = MOTOR()
        
        
        
        
        #pyrosim.Prepare_To_Simulate(robotId)
    def Run(self):     
        for t in range(1000):
            time.sleep(0.016)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            
    def Save_Values():
        #file save
        with open('data/backData.npy', 'wb') as f:
            numpy.save(f,self.robot.sensors())
            f.close



    def __del__(self):
        p.disconnect()

    

