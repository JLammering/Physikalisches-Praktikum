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

#Tiefe

#1 mm = 0.4 mikro s in Acryl
psi_acryl = 0.4

#1mm = 2/3 mikro s in der Flüssigkeit
psi_fluessig = 2/3

s_ausprisma = 30.7*psi_acryl
print(s_ausprisma)

s_breite = 10*2/3
print(s_breite)

psi_ms = 6/4
s_sss = 5*psi_ms
print(s_sss)
