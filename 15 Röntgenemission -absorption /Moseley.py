import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from uncertainties import ufloat
import uncertainties.unumpy as unp

E, Z = np.genfromtxt('Daten/Moseley.txt', unpack = True)
E = np.sqrt(E)

plt.plot(E, Z, 'k.', label = r'Messwerte')

slope, intercept, r_value, p_value, std_err = linregress(E, Z)

x = np.linspace(50,200)
plt.plot(x, slope*x + intercept, 'r-', label = r'Ausgleichsgerade')

slopem = ufloat(slope, std_err)

Rinf = 4/(3*slopem**2)

print("Steigung, Fehler:", slopem)
print("Rydbergkonstante:", Rinf)
plt.legend(loc = 'best')
plt.xlim(100,145)
plt.ylim(30, 43)
plt.grid()
plt.savefig('build/Moseley.pdf')
