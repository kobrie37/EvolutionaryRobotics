import copy
from sched import Event
from solution import SOLUTION
import constants as c
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del fitness*.txt")
        os.system("del brain*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

        
    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
 
    
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()   
        
        

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness < self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]
    
    def Print(self):
        for parent in self.parents:
            print("\n Parent: ",self.parents[parent].fitness," Child: ",self.children[parent].fitness, "\n")
        
    def Show_Best(self):
        best = 0
        iteration = 0
        for parent in self.parents:
            if self.parents[parent].fitness < best:
                best = self.parents[parent].fitness
                iteration = parent
        self.parents[iteration].Start_Simulation("GUI")
    
    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
