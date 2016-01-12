import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat


#große Kugel Zeit-Messwerte:
t = np.genfromtxt('datenappar.txt', unpack = True)

#Mittelwert:
a = np.mean(t)
z = (t-a)**2
w = np.mean(z)*4/3

#Abweichung:
T = ufloat(a, np.sqrt(w))
print('große Kugel Zeit-Mittelwert:', T)

#große Kugel Radius, Masse Werte:
D, M = np.genfromtxt('datendichtgr.txt', unpack = True)
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

#Viskosität(berechnet mit kleiner Kugel):
n = ufloat(0.001209, 0.000012)

#Apparaturkonstante:
K = n/(T*(p-P))
print('Apparaturkonstante:', K)
#Reynolds-Zahl:
l = 0.1
v = l/T
d = 2*r
Re = (p*v*d)/n
print('Reynolds-Zahl:', Re)
