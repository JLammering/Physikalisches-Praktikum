import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Daten:
t1,I1 = np.genfromtxt('Daten/Rhodium.txt',unpack='True')
t2,I2 = np.genfromtxt('Daten/Rhodium2.txt',unpack='True')
t1 = t1*20
t2 = t2*20

#Nullwert:
N0a = 195
N0b = 202
N0  = (N0a+N0b)/2
dN0 = np.sqrt((N0a-N0)**2 + (N0b-N0)**2)

#Anpassung Nullwert (20 s):
N0 = N0/45
dN0 = dN0/45
I1 = I1 - N0
I2 = I2 - N0

#Plot der Messwerte
plt.plot(t1,I1,'kx', label = r'Messwerte') #linke Hälfte
plt.plot(t2,I2,'kx') #rechte Hälfte
plt.plot((400,400),(1,1000),'r--', label = r'Grenze') # t*

plt.legend(loc='best')
plt.xlim(0,660)
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.yscale('log')
plt.grid()
plt.savefig('build/RhodiumM.pdf')
