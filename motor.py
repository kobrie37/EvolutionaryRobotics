import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act() 

    def Prepare_To_Act(self):
        print(f"Joint Name: {self.jointName}")
        
        if self.jointName == b'Torso_FrontLeg':
            self.amplitude = np.pi/3    
            self.frequency = 10 
            self.offset = 0   
        else:
            self.amplitude = np.pi/3    
            self.frequency = 5  
            self.offset = 0  


        self.time_steps = 1000
        
        self.targetAngles = np.linspace(0, 2 * np.pi, self.time_steps)
        
        self.motorValues = self.amplitude * np.sin(self.frequency * self.targetAngles + self.offset)    

 
    def Set_Value(self, robotId, t):
 
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],  
            maxForce=25
        )
