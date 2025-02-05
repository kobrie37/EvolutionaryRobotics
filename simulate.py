import pybullet as p 
import time 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

step = 1/45

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = np.zeros(1000)

for i in range(0, 1000, 1):
    p.stepSimulation()
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(step)
    #print(i)
p.disconnect() 

print(frontLegSensorValues)
np.save("FrontLegSensorValues.npy", frontLegSensorValues)
