import os as os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

for i in range(1):
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()
