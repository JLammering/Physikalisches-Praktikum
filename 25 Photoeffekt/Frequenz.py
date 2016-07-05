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

def mittelwert(sigma):#berechnet den mittelwert fehlerbehafteter Größen auf meine Weise :D
    l = len(sigma)
    sum = ufloat(0, 0)
    for i in range(0, l):
        sum += sigma[i]
    return (1/l)*sum

#Grundwerte:
c = 299792458

lamda, U, dU = np.genfromtxt('Daten/Frequenz.txt', unpack=True)

#Frequenz:
v = c*10**9/lamda
v = v * 10**(-14)

plt.errorbar(v,U,xerr=0,yerr=dU,fmt='kx', label=r'berechnete Wertepaare')

m, dm, b, db = linregress(v,U)
x = np.linspace(5,7.5)
plt.plot(x, m*x+b, 'r-', label= r'Ausgleichsgerade')

M = ufloat(m,dm)
B = ufloat(b,db)

plt.legend(loc='best')
print('Frequenz:',v)
print('Steigung,Abschnitt:', M, B)
plt.grid()
plt.xlabel(r'$\nu/\SI{e14}{\hertz}$')
plt.ylabel(r'$U/\si{\volt}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Frequenz.pdf')
