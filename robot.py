from os import link
from shlex import join
import pybullet as p
import os
from pyrosim.joint import JOINT
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f"del brain{solutionID}.nndf")

    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self,t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
            
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = bytes(self.nn.Get_Motor_Neurons_Joint(neuronName),'utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robot,desiredAngle)
                

    def Save_Values(self):
        for i in self.motors:
            self.motors[i].Save_Values()
        for i in self.sensors:
            self.sensors[i].Save_Values()
        
 
    def Think(self,t):
        self.nn.Update()
        #self.nn.Print()
        
    def Get_Fitness(self, ID):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open(f"tmp{ID}.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system(f"rename tmp{ID}.txt fitness{ID}.txt ")
        exit()
