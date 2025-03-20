import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system(f"python simulate.py {mode}")
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,.5] , size=[length,width,height])
        pyrosim.End()
    
    

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
    
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[1,0,1])
        pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
        pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[2,0,1])
        pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5] , size=[length,width,height])

        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
    
        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_Frontleg")
     
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName= currentRow, targetNeuronName= currentColumn+3, weight= self.weights[currentRow][currentColumn])

        pyrosim.End()
        
    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] = random.random() * 2 -1 

        
