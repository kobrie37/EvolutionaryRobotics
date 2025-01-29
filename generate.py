import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
y = 0 
z = 0.5

pyrosim.Start_SDF("boxes.sdf")

for k in range(10):
    for i in range(5):
        for j in range (5): 
                pyrosim.Send_Cube(name="Box", pos=[i,j,k] , size=[length,width,height])
    length *= .9
    width *= .9
    height *= .9
        
pyrosim.End()
