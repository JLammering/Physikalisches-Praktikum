import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import linregress

#Werte
T1, T2, t = np.genfromtxt('Daten/datentemp.txt', unpack=True)
T1 += 273.15
T2 += 273.15
t *= 60
#errT1 = 0.1
#errT2 = 0.1
#plt.errorbar(t, T1, yerr = errT1, fmt = 'kx', label = 'Messwerte T1')
#plt.errorbar(t, T2, yerr = errT2, fmt = 'bx', label = 'Messwerte T2')
plt.plot(t, T1, 'kx', label = 'Messwerte T1')
plt.plot(t, T2, 'bx', label = 'Messwerte T2')

#Ausgleichsrechnung
def f(t, A, B, C, D):
    return A*t**3 + B*t**2 + C*t + D

params1, covariance1 = curve_fit(f, t, T1)
errors1 = np.sqrt(np.diag(covariance1))

params2, covariance2 = curve_fit(f, t, T2)
errors2 = np.sqrt(np.diag(covariance2))

x_plot = np.linspace(0, 1200, 10000)
plt.plot(x_plot, f(x_plot, *params1), 'r-', label = 'Ausgleichskurve T1')
plt.plot(x_plot, f(x_plot, *params2), 'g-', label = 'Ausgleichskurve T2')
np.savetxt('build/tempcurve.txt', np.column_stack([params1[0], params1[1], params1[2], params1[3],
errors1[0], errors1[1], errors1[2], errors1[3],
params2[0], params2[1], params2[2], params2[3], errors2[0], errors2[1], errors2[2], errors2[3]]),
header = "A1, B1, C1, D1, dA1, dB1, dC1, dD1, A2, B2, C2, D2, dA2, dB2, dC2, dD2")

plt.ylabel(r'$T\:/\:\si{\kelvin}$')
plt.xlabel(r'$t\:/\:\si{\second}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plottemp.pdf')
