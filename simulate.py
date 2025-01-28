import pybullet as p 
import time 

physicsClient = p.connect(p.GUI)
step = 1/45

p.loadSDF("box.sdf")

for i in range(0, 1000, 1):
    p.stepSimulation
    time.sleep(step)
    print(i)
p.disconnect() 

p.configureDegugVisualizer(p.COV_ENABLE_GUI,0) 
