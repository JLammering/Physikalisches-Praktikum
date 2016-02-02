import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import linregress


#Werte
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 1.0, 2.1, 3.0, 4.0, 5.0])
plt.plot(x, y, 'kx', label = 'Messwerte')

#Curvefit
def f(x, a, b):
    return a * x + b

params, covariance = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance))

print('slope =', params[0], '±', errors[0])
print('y-Achsenab.', params[1], '±', errors[1])

slope = ufloat(params[0], errors[0])
x_plot = np.linspace(0, 5, 1000)
plt.plot(x_plot, f(x_plot, *params), 'b-', label = 'Ausgleichsgerade')
np.savetxt('build/testcurve.txt', np.column_stack([slope.n, params[1], slope.s, errors[1]]), header = "Steigung, b, Fehler Steigung, Fehler b")

#Werte mit Formel berechnen
m = (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
b = np.mean(y) - m*np.mean(x)
np.savetxt('build/testrech.txt', np.column_stack([m, b]), header = "m, b")

#linreg
slope, intercept, r_value, p_value, std_err = linregress(x, y)
data_x = np.linspace(0, 6, 1000)
error_b = std_err*np.mean(x**2)
plt.plot(data_x, slope*data_x+intercept, 'r-', label = 'Ausgleichsgerade linreg')
np.savetxt('build/testlin.txt', np.column_stack([slope, intercept, r_value, std_err, error_b]), header = "slope, y-Achsenab, r, Fehler Steigung, Fehler b")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/test.pdf')
