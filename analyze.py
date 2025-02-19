import numpy as np
import matplotlib.pyplot as plt

frontLegSensorValues = np.load("FrontLegSensorValues.npy")
backLegSensorValues = np.load("BackLegSensorValues.npy")
sinWave = np.load("SinWave.npy")
motorCommandsFL = np.load("MotorCommandsFrontLeg.npy")
motorCommandsBL = np.load("MotorCommandsBackLeg.npy")

'''plt.figure('Leg Sensor Values')
plt.plot(backLegSensorValues, label = "backLeg", linewidth = 3)
plt.plot(frontLegSensorValues, label = "frontLeg")
plt.legend()
plt.show()

plt.figure('Sine Wave')
plt.plot(sinWave)
plt.show()'''

plt.figure('Motor Commands')
plt.plot(motorCommandsFL)
plt.plot(motorCommandsBL)
plt.show()
