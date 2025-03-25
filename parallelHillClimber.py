from solution import SOLUTION
import copy
import constants as c
import os as os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del fitness*.txt")
        os.system("del brain*.nndf")
        
        self.parents = {}

        self.nextAvailableID = 0 
        
        for p in range(c.populationSize):
            self.parents[p] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for p in self.parents:
            self.children[p] = copy.deepcopy(self.parents[p])
            self.children[p].Set_ID(self.nextAvailableID)
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
        for p in solutions:
            solutions[p].Start_Simulation("GUI")
        for p in solutions:
            solutions[p].Wait_For_Simulation_To_End()
