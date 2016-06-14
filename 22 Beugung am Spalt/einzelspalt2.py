import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit


Ispalt1, Ispalt2, Ispalt3 = np.genfromtxt('daten/einzelspalte.txt',unpack = 'True')
x = np.genfromtxt('daten/abstandeinzelspalt.txt',unpack = 'True')
Ispalt2 *= 1e-6
Ispalt2 -= 1.45e-9#dunkelstrom abziehen
L = 1 #Abstand Spalt-Ebene
lamda = 633e-9#Wellenlänge He-Ne

x *= 1e-3#in millimeter umrechnen
x -= 27e-3
print('x= ',x)
phi = x/L
def f(phi, A_0, b):
    return (A_0**2 * b**2 *(lamda/(np.pi*b*np.sin(phi)))**2 * (np.sin(np.pi*b*np.sin(phi)/lamda))**2)

params, covariance = curve_fit(f, phi, Ispalt2, p0=[6, 0.15e-3])

errors = np.sqrt(np.diag(covariance))

print('A_0 =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


x_plot = np.linspace(-15e-3, 15e-3, 10000)
phi_plot = (x_plot/L)
plt.plot(x_plot, f(x_plot, *params)*1e6, 'b-', label = 'Ausgleichsgerade')
b = ufloat(params[1], errors[1])

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)
print('abweichung = ', abweichung(params[1], 0.15e-3)*100)


plt.plot(x, Ispalt2*1e6, 'kx', label = 'Messwerte')
plt.xlabel(r'$\varphi \:/\: \si{\radian}$')
plt.ylabel(r'$(I-I_0) \:/\: \si{\micro\ampere}$')

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/einzelspalt2.pdf')
plt.show()
