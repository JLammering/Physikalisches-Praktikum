import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit


Idoppel = np.genfromtxt('daten/doppelspalt.txt',unpack = 'True')
Idoppel *= 1e-6
Idoppel -= 1.45e-9#dunkelstrom abziehen
L = 1 #Abstand Spalt-Ebene
lamda = 633e-9#Wellenlänge He-Ne

xalt = np.zeros(81)
xalt[0] = 15
print('maximum = ',Idoppel[45])
for i in range(1, 81):#Positionswerte erzeugen
    xalt[i] = xalt[i-1] + 0.25
    # if Idoppel[i] == 2.8e-6:
    #     #x[i] = 27.1
    #     print('Maximum bei i= ',i)

print(xalt)

xalt *= 1e-3#in millimeter umrechnen
print('x beim Maximum', xalt[45])
xalt -= 26.25e-3
np.savetxt('build/abstanddoppel.txt', np.column_stack([xalt]),
header="Abstand Doppel")
x = np.genfromtxt('daten/abstanddoppel.txt',unpack = 'True')
print('x= ',x)
phi = x/L

def f(phi, A_0, s, b):
    return (A_0 * (np.cos((np.pi*s*np.sin(phi))/lamda))**2 *(lamda/(np.pi*b*np.sin(phi)))**2 * (np.sin(np.pi*b*np.sin(phi)/lamda))**2)

params, covariance = curve_fit(f, phi, Idoppel, p0=[3e-6, 0.5e-3, 0.1e-3])

errors = np.sqrt(np.diag(covariance))

print('A_0 =', params[0], '±', errors[0])
print('s =', params[1], '±', errors[1])
print('b = ', params[2], '±', errors[2])


x_plot = np.linspace(-10e-3, 10e-3, 10000)
phi_plot = (x_plot/L)
plt.plot(phi_plot, f(phi_plot, *params)*1e6, 'b-', label = 'Ausgleichsgerade')
b = ufloat(params[1], errors[1])

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)
print('abweichung s= ', abweichung(params[1], 0.5e-3)*100)
print('abweichung b= ', abweichung(params[2], 0.1e-3)*100)



plt.plot(phi, Idoppel*1e6, 'kx', label = 'Messwerte')
plt.xlabel(r'$\varphi \:/\: \si{\radian}$')
plt.ylabel(r'$(I-I_0) \:/\: \si{\micro\ampere}$')

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/doppelspalt.pdf')
plt.show()
