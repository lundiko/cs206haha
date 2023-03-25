import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import pybullet_data
import os
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR
class ROBOT:

    
    def __init__(self, solutionID): 
        self.robotId = (p.loadURDF("body.urdf"))
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.solutionID = solutionID
        self.brainID = "brain" + str(solutionID) + ".nndf"
        self.nn = NEURAL_NETWORK(self.brainID)
        os.system("del "+ self.brainID)

        
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        nameFitness = "tmp" + str(self.solutionID) + ".txt"
        f = open(nameFitness, "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename " + nameFitness + " fitness" + str(self.solutionID)+ ".txt")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for sensor in self.sensors.values():
            sensor.GetValue(t)
        
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
                self.motors[jointName] = MOTOR(jointName)
            
    def Act(self, robot):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(robot, desiredAngle)
                #jointName.setValue(robot, desiredAngle)
                
        #for motor in self.motors.values():
           # 
        
    def Think(self):
        self.nn.Update()
