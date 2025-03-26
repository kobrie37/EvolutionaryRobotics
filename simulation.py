from cmath import phase
from math import pi
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c

from world import WORLD
from robot import ROBOT

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
                
        for t in range(c.numberOfTimeSteps):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think(t)
            self.robot.Act(t)

            if self.GUI == True:
                time.sleep(c.num_steps)
            
            
    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)
           
    def __del__(self): 
        p.disconnect()
