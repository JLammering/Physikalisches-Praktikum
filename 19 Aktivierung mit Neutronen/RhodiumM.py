import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Daten:
t1,I1 = np.genfromtxt('Daten/Rhodium.txt',unpack='True')
t2,I2 = np.genfromtxt('Daten/Rhodium2.txt',unpack='True')
t1 = t1*20
t2 = t2*20

#Nullwert:
N0 = 195/900

#Anpassung Nullwert (20 s):
N0 = N0*20

I1 = I1-N0
I2 = I2-N0

#Plot der Messwerte
plt.errorbar(t1,I1,xerr=0,yerr=np.sqrt(I1), fmt='kx', label = r'Messwerte') #linke Hälfte
plt.errorbar(t2,I2,xerr=0,yerr=np.sqrt(I2), fmt='kx') #rechte Hälfte
plt.plot((400,400),(1,1000),'r--', label = r'Grenze') # t*

tz = np.array([340, 360, 380])
Iz = np.array([36, 36, 40])
Iz = Iz-N0
plt.errorbar(tz,Iz,xerr=0,yerr=np.sqrt(Iz),fmt = 'kx')

plt.legend(loc='best')
plt.xlim(0,720)
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.yscale('log')
plt.grid()
plt.savefig('build/RhodiumM.pdf')
