import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c


length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

        
    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"start /B python simulate.py {mode} {self.myID}")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        time.sleep(0.01)
        fitnessFile = open(f"fitness{self.myID}.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system(f"del fitness{self.myID}.txt")
        
    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 -1 
        
    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,.5] , size=[length,width,height])
        pyrosim.End()
    
    


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
    
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])

        pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[0,-0.5,1], jointAxis="1 0 0")
    
        pyrosim.Send_Cube(name="Backleg", pos=[0, -0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[0,0.5,1], jointAxis="1 0 0")
    
        pyrosim.Send_Cube(name="Frontleg", pos=[0, 0.5, 0] , size=[0.2, 1, 0.2])
        
        pyrosim.Send_Joint(name="Torso_Leftleg", parent="Torso", child="Leftleg", type="revolute", position=[-0.5,0,1], jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="Leftleg", pos=[-0.5, 0, 0] , size=[1, 0.2, 0.2])
        
        pyrosim.Send_Joint(name="Torso_Rightleg", parent="Torso", child="Rightleg", type="revolute", position=[0.5,0,1], jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="Rightleg", pos=[0.5, 0, 0] , size=[1, 0.2, 0.2])
        
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="Frontleg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="Backleg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="Leftleg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])
        
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="Rightleg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5] , size=[0.2, 0.2, 1])

        pyrosim.End()
        

        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        
        nameCount = 0
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "Torso")
        nameCount+=1
    
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "Backleg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "Frontleg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "Leftleg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "Rightleg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "FrontLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "BackLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "LeftLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Sensor_Neuron(name = nameCount, linkName = "RightLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "Torso_Backleg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "Torso_Frontleg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "Torso_Leftleg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "Torso_Rightleg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "FrontLeg_FrontLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "BackLeg_BackLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "LeftLeg_LeftLowerLeg")
        nameCount+=1
        
        pyrosim.Send_Motor_Neuron(name = nameCount, jointName = "RightLeg_RightLowerLeg")
        nameCount+=1
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn+c.numSensorNeurons, weight= self.weights[currentRow][currentColumn])

        pyrosim.End()
     
