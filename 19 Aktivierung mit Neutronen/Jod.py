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
N0a = 195
N0b = 202
N0  = (N0a+N0b)/2
dN0 = np.sqrt((N0a-N0)**2 + (N0b-N0)**2)

#Anpassung Nullwert (200 s):
N0 = N0/4.5
dN0 = dN0/4.5

I = I - N0

plt.plot(t, I,'kx', label = r'Messwerte')
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
'Nulleffekt', N0, dN0,
'N(0):', Ne,
'Vorfaktor', Nn
)

plt.legend(loc='best')
plt.grid()
plt.ylabel(r'P')
plt.xlabel(r't/\si{\second}')
plt.yscale('log')
plt.savefig('build/Jod.pdf')
