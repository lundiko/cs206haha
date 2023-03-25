from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range (c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        

    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].First_Sim("DIRECT")
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
        for currentGeneration in range(c.numberOfGenerations):
                self.Evolve_For_One_Generation( )

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    
    def Select(self):
        for key in self.parents:
            if(self.children[key].fitness < self.parents[key].fitness):
                self.parents[key] = self.children[key]

    def Evaluate(self, solutions):
        for j in solutions:
            solutions[j].Start_Simulation("DIRECT")
        for k in solutions:
            solutions[k].Wait_For_Simulation_To_End()

    def Print(self):
        print("")
        for key in self.parents:
            print("Parent: "+ str(self.parents[key].fitness) + "  Child: " + str(self.children[key].fitness))
        print("")

    def Show_Best(self):
        x = self.parents[0]
        for parent in self.parents:
            if(x.fitness < self.parents[parent].fitness):
                x = self.parents[parent]
        x.Start_Simulation("GUI")