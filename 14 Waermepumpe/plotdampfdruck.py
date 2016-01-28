
# V203
# Graph von Temperatur und Druck (< 1bar)
# Lineare Regression: Angabe von Steigung, Abschnitt und Fehler
# Messwerte aus der Datei 'V203Daten1.txt'

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

# Messwerte:
y, x = np.genfromtxt('Daten/datendampfdruck.txt', unpack=True)
y = np.log(y)
x = 1/(x+273.15)
plt.plot(x, y, 'kx', label = 'Messwerte')

# Curve Fit linear:
def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))


print('-L/R =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x_plot = np.linspace(0.003, 0.0046, 1000)
plt.plot(x_plot, f(x_plot, *params), 'b-', label = 'Ausgleichsgerade')
slope = ufloat(params[0], errors[0])
R = ufloat(8.3144598, 0.0000048)
L = - slope * R
np.savetxt('build/dampfdruck.txt', np.column_stack([slope.n, R.n, L.n, slope.s, R.s, L.s]), header = "Steigung, R, L, Fehler Steigung, Fehler R, Fehler L")

# Ausgabe:

plt.xlabel(r'$(T\:/\:\si{\kelvin})^{-1}$')
plt.ylabel(r'$\mathrm{ln}(p\:/\:\si{bar})$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotdampfdruck.pdf')
