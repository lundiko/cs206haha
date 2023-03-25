import constants as c
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
import time
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
class SIMULATION:
    def __init__(self,directOrGUI,solutionID):
        if(directOrGUI == "DIRECT"):
            physicsClient = p.connect(p.DIRECT) #p.GUI
        else:
            physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.GRAVITY)
        self.solutionID = solutionID
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        self.directOrGUI = directOrGUI
        #self.sensor = SENSOR()
        #self.motor = MOTOR()
        
        
        
        
        #pyrosim.Prepare_To_Simulate(robotId)
    def Run(self):     
        for t in range(1000):
            if (self.directOrGUI == "GUI"): 
                time.sleep(0.016)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(self.robot)
            
    def Save_Values(self):
        #file save
        with open('data/backData.npy', 'wb') as f:
            numpy.save(f,self.robot.sensors())
            f.close


    def Get_Fitness(self):
        self.robot.Get_Fitness()
    
    def __del__(self):
        p.disconnect()

    

