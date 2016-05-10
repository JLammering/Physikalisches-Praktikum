import matplotlib.pyplot as plt
import numpy as np

#Schallgeschwindigkeiten
cl = 1800
cp = 2700

#Prismenwinkel in Grad:
t1 = 15
t2 = 30
t3 = 60

#Dopplerwinkel:
a1 = 90 - 360*np.arcsin(np.sin(t1*2*np.pi/360)*cl/cp)/(2*np.pi)
a2 = 90 - 360*np.arcsin(np.sin(t2*2*np.pi/360)*cl/cp)/(2*np.pi)
a3 = 90 - 360*np.arcsin(np.sin(t3*2*np.pi/360)*cl/cp)/(2*np.pi)

print('Dopplerwinkel:', a1, a2, a3)
