import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

def linregress(x, y):
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error

#Daten:
t, I = np.genfromtxt('Daten/Jod.txt',unpack = 'True')
t = t*200

#Nullwert:
N0 = 195/900

#Anpassung Nullwert (200 s):
N0 = N0*200

I = I - N0


plt.errorbar(t, I, xerr = 0, yerr = np.sqrt(I), fmt = 'kx', label = r'Messwerte')
m, dm, b, db = linregress(t, np.log(I))
x = np.linspace(0,3000)
plt.plot(x, np.exp(m*x+b), 'r-', label = r'Ausgleichsfunktion')

M = ufloat(m,dm)
B = ufloat(b,db)
Ne = ufloat(np.exp(b),db*np.exp(6.28))
Nn = Ne*(1-np.exp(200*m))
T = -np.log(2)/M

print(
'Halbwertszeit:', T,
'Steigung:',M,
'Verschiebung:',B,
'Nulleffekt', N0,
'N(0):', Ne,
'Vorfaktor', Nn,
'Messwerte mit Nulleffekt:',I,
'Poisson-Fehler:',np.sqrt(I)
)

plt.legend(loc='best')
plt.grid()
plt.ylabel(r'P')
plt.xlabel(r't/\si{\second}')
plt.yscale('log')
plt.savefig('build/Jod.pdf')
