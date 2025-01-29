import pybullet as p 
import time 
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

step = 1/45

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

for i in range(0, 1000, 1):
    p.stepSimulation()
    time.sleep(step)
    print(i)
p.disconnect() 

