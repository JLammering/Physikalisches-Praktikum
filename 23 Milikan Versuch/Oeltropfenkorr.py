import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

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

#Grundwerte:
B = 6.17*10**(-5)/760

#Daten für Radius und Ladung:
q,dq,r,dr = np.genfromtxt('Daten/Korr.txt', unpack=True)

Q = unp.uarray(q,dq)
R = unp.uarray(r,dr)
R = R*10**(-7)

#korrigierte Ladung(*10^-19):
Qk = Q*(1+B/R)**(3/2)

print('korrigierte Ladungen(10^-19):', Qk)

Qkm=[5.4, 11.9, 4.4, 9.9, 12.6, 18.9]
Qke=[0.4, 2.4, 1.3, 0.9, 5.2, 5.1]

a = [3,7,3,6,8,12]

plt.errorbar(a, Qkm, xerr=0, yerr=Qke,fmt='kx', label = r'gewertete Ladungen')
plt.errorbar(3,5.0,xerr=0,yerr=1.8, fmt= 'rx', label = r'nicht gewertete Ladungen')
m,dm,b,db = linregress(a,Qkm)
x = np.linspace(0,16)
plt.plot(x, m*x+b, label = r'Ausgleichsgerade')
M = ufloat(m,dm)
B = ufloat(b,db)
F = ufloat(96485.3329,0.0006)
print('Steigung,Abschnitt', M,B,
'Avogadro:',F*10**(19)/M)

plt.legend(loc = 'best')
plt.xlabel(r'$gV$')
plt.ylabel(r'$q/\si{\coulomb}$')
plt.grid(True, linewidth=0.16)
plt.xlim(0,16)
plt.ylim(0,25)
plt.savefig('build/korr.pdf')
