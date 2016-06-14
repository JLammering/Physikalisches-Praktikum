import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit


Ispalt1, Ispalt2, Ispalt3 = np.genfromtxt('daten/einzelspalte.txt',unpack = 'True')
x = np.genfromtxt('daten/abstandeinzelspalt.txt',unpack = 'True')

Ispalt1 *= 1e-6
Ispalt1 -= 1.45e-9#dunkelstrom abziehen
L = 1 #Abstand Spalt-Ebene
x_0 = 0.027#Position des Maximums
lamda = 633e-9#Wellenlänge He-Ne
#print('sin(pi/2)= ',np.sin(np.pi/2))

# x = np.zeros(51)
# x[0] = 12.5
# for i in range(1, 51):#Positionswerte erzeugen
#     if i =
#     x[i] = x[i-1] + 0.5
#     if x[i] == 27:
#         #x[i] = 27.1
#         print('Maximum bei i= ',i)
#
x *= 1e-3#in millimeter umrechnen
phi = (x-x_0)/L#Winkel bestimmen
phi = (phi/360)*2*np.pi#in rad umrechnen




#Curve Fit:
#phi[29] = 0.00001
#np.delete(phi,29)#nicht durch null teilen
#print('phi= ',phi)

def f(x, A_0, b):
    return (A_0**2 * b**2 *(lamda/(np.pi*b*(x-x_0)/L))**2 * np.sin((np.pi*b*(x-x_0)/L)/lamda)**2)

params, covariance = curve_fit(f, x, Ispalt1,p0=[1e-6, 0.000075])

errors = np.sqrt(np.diag(covariance))

print('A_0 =', params[1], '±', errors[1])
print('b =', params[2], '±', errors[2])
print('x_0=', params[0])
x_0 = params[0]
phi = (x-x_0)/L


x_plot = np.linspace(12e-3, 37e-3, 1000)
plt.plot((x_plot-x_0)/L, f(x_plot, *params), 'b-', label = 'Ausgleichsgerade')
b = ufloat(params[2], errors[2])


plt.plot(phi, Ispalt1, 'kx', label = 'Messwerte')
plt.xlabel(r'$\varphi \:/\: 1$')
plt.ylabel(r'$(I-I_0) \:/\: \si{\micro\ampere}$')

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/einzelspalt1.pdf')
