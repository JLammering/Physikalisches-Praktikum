import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit


Ispalt1, Ispalt2, Ispalt3 = np.genfromtxt('daten/einzelspalte.txt',unpack = 'True')
x = np.genfromtxt('daten/abstandeinzelspalt.txt',unpack = 'True')
Ispalt1 *= 1e-6
Ispalt1 -= 1.45e-9#dunkelstrom abziehen
L = 1 #Abstand Spalt-Ebene
#x_0 = 0.027#Position des Maximums
lamda = 633e-9#Wellenlänge He-Ne
#print('sin(pi/2)= ',np.sin(np.pi/2))

# x = np.zeros(51)
# x[0] = 12.5
# for i in range(1, 51):#Positionswerte erzeugen
#     x[i] = x[i-1] + 0.5
#     if x[i] == 27:
#         #x[i] = 27.1
#         print('Maximum bei i= ',i)
#
# print(x)

x *= 1e-3#in millimeter umrechnen
x -= 27e-3
print('x= ',x)
phi = x/L
#phi = (x-x_0)/L#Winkel bestimmen
#phi = (phi/360)*2*np.pi#in rad umrechnen




#Curve Fit:
#phi[29] = 0.00001
#np.delete(phi,29)#nicht durch null teilen
#print('phi= ',phi)

def f(phi, A_0, b):
    return (A_0**2 * b**2 *(lamda/(np.pi*b*np.sin(phi)))**2 * (np.sin(np.pi*b*np.sin(phi)/lamda))**2)

params, covariance = curve_fit(f, phi, Ispalt1, p0=[6, 1e-4])

errors = np.sqrt(np.diag(covariance))

print('A_0 =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
#print('x_0=', params[0])
#x_0 = params[0]
#phi = (x-x_0)/L


x_plot = np.linspace(-15e-3, 15e-3, 10000)
phi_plot = (x_plot/L)
plt.plot(x_plot, f(x_plot, *params)*1e6, 'b-', label = 'Ausgleichsgerade')
b = ufloat(params[1], errors[1])

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)
print('abweichung = ', abweichung(params[1], 0.075e-3)*100)


plt.plot(x, Ispalt1*1e6, 'kx', label = 'Messwerte')
plt.xlabel(r'$\varphi \:/\: \si{\radian}$')
plt.ylabel(r'$(I-I_0) \:/\: \si{\micro\ampere}$')

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/einzelspalt1.pdf')
plt.show()
