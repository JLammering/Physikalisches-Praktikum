import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

U, I1, I2, I3, I4, I5 = np.genfromtxt('daten/kennlinien.txt',unpack = 'True')

def minusvierwerte(x):
    b = len(x)
    y = np.zeros(b-4)
    for i in range(0, b-4):
        y[i] = x[i]
    return(y)
# print('Uminus4 = ', minusvierwerte(U))

U = minusvierwerte(U)
I1 = minusvierwerte(I1)*1e-3#in mA umrechnen

def f(U, a, b):
    return (a*U**b)

params, covariance = curve_fit(f, U, I1, p0=[1, 1])

errors = np.sqrt(np.diag(covariance))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x_plot = np.linspace(0, 220, 10000)

plt.plot(U, I1*1e3, 'kx', label = 'Messwerte $I_1$')
plt.plot(x_plot, f(x_plot, *params)*1e3, 'b-', label = 'Ausgleichskurve')

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)
print('abweichung = ', abweichung(params[1], 1.5)*100)

plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$I \:/\: \si{\milli\ampere}$')
plt.xlim(0, 220)

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/raumladung.pdf')
