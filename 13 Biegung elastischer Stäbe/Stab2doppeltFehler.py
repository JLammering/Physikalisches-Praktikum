# zweiseitig eingespannter quadratischer Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

# Messwerte für Abstand, linksOhneGew, rechtsOhneGew, linksMitGew, rechtsMitGew:
x, dlog, drog, dlmg, drmg = np.genfromtxt('Stab2doppelt.txt', unpack = True)
x = x/100
dl = (dlog-dlmg)/1000
dr = (drog-drmg)/1000
L = 0.55
dl = dl[::-1]
#xr = 0.275 + x
dr = dr[::-1]


#plt.plot(dr, 4*xr**3 - 12*L*xr**2 + 9*L**2*xr - L**3, 'k.')
plt.plot(dl, 3*(L**2)*x - 4*x**3, 'r.')
plt.plot(dr, 3*(L**2)*x - 4*x**3, 'k.')


plt.savefig('Stab2doppeltFehler.pdf')
