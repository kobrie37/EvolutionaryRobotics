import os as os
from hillclimber import HILL_CLIMBER

for i in range(1):
    hc = HILL_CLIMBER()
    hc.Evolve()
    hc.Show_Best()

