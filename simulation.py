from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import pybullet_data

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):

        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            self.GUI = False
        else:
            self.physicsClient = p.connect(p.GUI)
            self.GUI = True
            
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setGravity(0,0,-9.8)
        
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for t in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think(t)
            self.robot.Act(t)
    
            if self.GUI == True:
                time.sleep(c.step)
    
            
    def Save_Values(self):
        np.save("FrontLegSensorValues.npy", frontLegSensorValues)
        np.save("BackLegSensorValues.npy", backLegSensorValues)
        np.save("SinWave.npy", sinWaveVector)
        np.save("MotorCommandsFrontLeg.npy", motorCommandsFrontLeg)
        np.save("MotorCommandsBackLeg.npy", motorCommandsBackLeg)
        
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)
        
