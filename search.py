import os as os
from hillclimber import HILL_CLIMBER 

for i in range(1):
    hc = HILL_CLIMBER()

    hc.Evolve()
    hc.Show_Best()
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")
