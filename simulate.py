import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
import sys

from simulation import SIMULATION
from world import WORLD
from robot import ROBOT

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()


