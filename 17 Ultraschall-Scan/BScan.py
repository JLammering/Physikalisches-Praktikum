import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Schallgeschwindigkeit:
c = 2730

#Höhe des Blocks:
h = 8.04

#Laufzeiten/us:
t1, t2, slit ,dlit = np.genfromtxt('Daten/BScanLz.txt', unpack = 'True')
t1 = (t1-3)/2
t2 = (t2-3)/2

#Strecken/cm:
s1 = c*t1*10**(-4)
s2 = c*t2*10**(-4)

#Durchmesser/cm:
d = h - s1 - s2

#Ausgabe:
print(
'Strecken1:',s1,
'Strecken2:',s2,
'Durchmesser:',d
)

#VGL mit Litwerten:
deltas = np.abs(100*(slit-s2)/slit)
deltad = np.abs(100*(dlit-d)/dlit)
print(
'relativer Fehler(Strecke BScan):', deltas,
'relativer Fehler(Dicke BScan):', deltad
)
