import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
#size = [ len, w, h ]
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,2,3])
pyrosim.End()
