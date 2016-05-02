import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import linregress
import uncertainties.unumpy as unp

phi, lamda, t = np.genfromtxt('Daten/eichung.txt', unpack=True)
phi *= (1/360)*2*np.pi #in rad umrechnen

phi_01 = np.array([phi[0],phi[1]])#phi in array
#print(phi_12, np.mean(phi_12), np.std(phi_12))
phi_gem1 = ufloat(np.mean(phi_01), np.std(phi_01))#phi mitteln
lamda_0_1  = lamda[0]-lamda[1]

eich1 = (abs(lamda[0]-lamda[1])/(abs(t[0]-t[1]))*unp.cos(phi_gem1))#erste eichgroesse
print(eich1)

phi_23 = np.array([phi[2],phi[3]])
#print(phi_12, np.mean(phi_12), np.std(phi_12))
phi_gem2 = ufloat(np.mean(phi_23), np.std(phi_23))
lamda_2_3 = lamda[2]-lamda[3]

eich2 = (abs(lamda[2]-lamda[3])/(abs(t[2]-t[3]))*unp.cos(phi_gem2))
print(eich2)

eichgroesse = (1/2)*(eich1 + eich2)
print(eichgroesse)
np.savetxt('build/eichgroesse.txt', np.column_stack([eich1.n, eich1.s, phi_gem1.n, phi_gem1.s, lamda_0_1, eich2.n, eich2.s, phi_gem2.n, phi_gem2.s, lamda_2_3, eichgroesse.n, eichgroesse.s]), header = "eichgroesse1, Fehler eichgroesse1, phi_gem1, Fehler phi_gem1, lamda_0-1, eichgroesse2, Fehler eichgroesse2, phi_gem2, Fehler phi_gem2, lamda_2_3, eichgroesse, Fehler eichgroesse")
