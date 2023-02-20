import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import numpy
class MOTOR:

    def __init__(self,jointName):
        self.jointName = jointName
        print(jointName)
        self.values = numpy.zeros(c.ANGLEVALUES)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if (self.jointName == "Torso_BackLeg"):
            self.amplitude = c.AMPLITUDE
            self.frequency = c.FREQUENCY
            self.offset = c.OFFSET
            x = numpy.linspace((0), (2*numpy.pi), 1000)
            count = 0
            for j in x:
                self.values[count] = self.amplitude * numpy.sin(self.frequency * j +self.offset)
                count +=1
        else:
            self.amplitude = c.AMPLITUDE
            self.frequency = c.FREQUENCY/2
            self.offset = c.OFFSET
            x = numpy.linspace((0), (2*numpy.pi), 1000)
            count = 0
            for j in x:
                self.values[count] = self.amplitude * numpy.sin(self.frequency * j +self.offset)
                count +=1
            
    def Set_Value(self,robotId, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            #had the KeyError problem
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.values[t],
            maxForce = c.FORCE)



        
        
      

        
