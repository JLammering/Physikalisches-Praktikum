import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#kleine Kugel Zeit-Messwerte:
t = np.genfromtxt('datenviskos.txt', unpack = True)

#Mittelwert:
a = np.mean(t)
z = (t-a)**2
w = np.mean(z)*4/3

#Abweichung:
T = ufloat(a, np.sqrt(w))
print('kleine Kugel Zeit-Mittelwert:', T)

#kleine Kugel Dichte-Messwerte:
D, M = np.genfromtxt('datendichtkl.txt', unpack = True)
M = M*10**(-3)
R = 0.5*D*10**(-3)

#Mittelwert und Fehler:
a = np.mean(R)
m = np.mean(M)

z = (R-a)**2
w = np.mean(z)*4/3
print('Radius-abweichung vom Mittelwert:', np.sqrt(w))

r = ufloat(a, np.sqrt(w))

V = 4/3 * np.pi * r**3

#Dichte:
p = m/V
print('Dichte:', p, 'Masse:', m, 'Radius:', r,'Volumen:',V)
P = 998.2

#Apparaturkonstante kleine Kugel:
K = 0.07640 * 10**(-6)

#Viskosität:
n = K*(p-P)*T
print('Viskosität:', n)
