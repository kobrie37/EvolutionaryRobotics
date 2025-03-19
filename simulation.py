from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import pybullet_data

class SIMULATION:
    def __init__(self, directOrGUI):

        if directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            self.GUI = True
        else:
            self.physicsClient = p.connect(p.DIRECT)
            self.GUI = False

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for t in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
    
            if self.GUI == True:
                time.sleep(c.step)
            
    def Save_Values(self):
        np.save("FrontLegSensorValues.npy", frontLegSensorValues)
        np.save("BackLegSensorValues.npy", backLegSensorValues)
        np.save("SinWave.npy", sinWaveVector)
        np.save("MotorCommandsFrontLeg.npy", motorCommandsFrontLeg)
        np.save("MotorCommandsBackLeg.npy", motorCommandsBackLeg)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
    def __del__(self):
        p.disconnect()
        
