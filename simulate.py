import pybullet as p 
import time 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

step = 1/45
num_steps = 1000

amplitudeFrontLeg = np.pi / 4  
frequencyFrontLeg = 3 * np.pi  
phaseOffsetFrontLeg = np.pi / 2 

amplitudeBackLeg = np.pi / 4
frequencyBackLeg = 3 * np.pi 
phaseOffsetBackLeg = - np.pi / 2

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")

robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

frontLegSensorValues = np.zeros(num_steps)
backLegSensorValues = np.zeros(num_steps)

sinWaveVector = np.zeros(num_steps)

motorCommandsFrontLeg = amplitudeFrontLeg * np.sin(2 * np.pi * frequencyFrontLeg * np.arange(num_steps) / num_steps + phaseOffsetFrontLeg)
motorCommandsBackLeg = amplitudeBackLeg * np.sin(2 * np.pi * frequencyBackLeg * np.arange(num_steps) / num_steps + phaseOffsetBackLeg)

for i in range(num_steps):
    p.stepSimulation()
    
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="BackLeg_Torso",
        controlMode=p.POSITION_CONTROL,
        targetPosition=motorCommandsBackLeg[i],
        maxForce=25
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=motorCommandsFrontLeg[i],
        maxForce=25
    )

    #sinWaveVector[i] = np.sin(targetAngles)
    
    time.sleep(step)

p.disconnect() 

np.save("FrontLegSensorValues.npy", frontLegSensorValues)
np.save("BackLegSensorValues.npy", backLegSensorValues)
np.save("SinWave.npy", sinWaveVector)
np.save("MotorCommandsFrontLeg.npy", motorCommandsFrontLeg)
np.save("MotorCommandsBackLeg.npy", motorCommandsBackLeg)
