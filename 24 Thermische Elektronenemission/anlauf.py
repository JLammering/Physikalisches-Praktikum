import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

e = ufloat(1.6021766208e-19, 0.0000000098e-19)#C
k = ufloat(1.38064852e-23, 0.00000079e-23)#J/K

U, I = np.genfromtxt('daten/anlauf.txt',unpack = 'True')
I = I*1e-9

def Ukorr(U, I, R):
    Uk = U - I*R
    return(Uk)

Uk = Ukorr(U, I, 10**6)
Uk *= -1

def f(U, c, d):
    return (c*np.exp(d*U))

params, covariance = curve_fit(f, Uk, I, p0=[1, 1])

errors = np.sqrt(np.diag(covariance))

print('c =', params[0], '±', errors[0])
print('d =', params[1], '±', errors[1])
d = ufloat(params[1], errors[1])
T = (e/(k*d))
print('T = ', T)
print('U_korrekt = ', Uk)
#np.savetxt('build/anlauf.txt', np.column_stack([U, Uk, I*1e9]), header = "U/V U_korrekt/V, I/nA")


x_plot = np.linspace(-1, 0.2, 10000)

plt.plot(Uk, I*1e+9, 'kx', label = 'Messwerte')
plt.plot(x_plot, f(x_plot, *params)*1e+9, 'b-', label = 'Ausgleichskurve')


plt.legend(loc='best')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$I \:/\: \si{\nano\ampere}$')
plt.ylim(0,15)
plt.xlim(-1,0.05)

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/anlauf.pdf')
