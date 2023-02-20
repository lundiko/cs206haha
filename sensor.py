import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import numpy
class SENSOR:

    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.SENSORVALUES)

    def GetValue(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (t == 999):
            print(self.values)

