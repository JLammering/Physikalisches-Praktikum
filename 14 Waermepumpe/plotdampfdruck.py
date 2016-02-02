

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import linregress

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
np.savetxt('build/dampfdruckcurve.txt', np.column_stack([slope.n, R.n, L.n, params[1], slope.s, R.s, L.s, errors[1]]), header = "Steigung, R, L, b, Fehler Steigung, Fehler R, Fehler L, Fehler b")

#linreg
slope, intercept, r_value, p_value, std_err = linregress(x, y)
data_x = np.linspace(0.003, 0.0046, 1000)
error_b = std_err*np.mean(x**2)
#plt.plot(data_x, slope*data_x+intercept, 'r-', label = 'Ausgleichsgerade')
np.savetxt('build/dampfdrucklinreg.txt', np.column_stack([slope, intercept, r_value, std_err, error_b]), header = "slope, y-Achsenab, r, Fehler Steigung, Fehler b")

# Ausgabe:

plt.xlabel(r'$(T\:/\:\si{\kelvin})^{-1}$')
plt.ylabel(r'$\mathrm{ln}(p\:/\:\si{bar})$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotdampfdruck.pdf')
