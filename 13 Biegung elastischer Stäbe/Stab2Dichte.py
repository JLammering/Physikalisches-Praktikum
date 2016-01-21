# Dichte des quadratischen Stabes
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Länge, Durchmesser und Masse:
l, d = np.genfromtxt('Stab2Dichte.txt', unpack=True)
d = d/1000
m = 0.1641

#Mittelwerte und Standardabweichung:
ml = np.mean(l)
md = np.mean(d)

dl = np.sqrt((10/9)*np.mean((l-ml)**2))
dd = np.sqrt((10/9)*np.mean((d-md)**2))

L = ufloat(ml, dl)
D = ufloat(md, dd)

#Volumen:
V = D**2 * L

#Dichte:
p = m/V

#Ausgabe:
print('quadratischer Stab:',
'Mittelwert Länge:', L,
'Mittelwert Durchmesser:', D,
'Volumen:', V,
'Dichte:' , p)
