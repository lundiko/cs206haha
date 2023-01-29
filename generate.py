import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x = 0
y = 0
z = .5
#size = [ len, w, h ]
pyrosim.Send_Cube(name="Box", pos=[x,y,z,.5] , size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1,.5] , size=[1,1,1])
pyrosim.End()
