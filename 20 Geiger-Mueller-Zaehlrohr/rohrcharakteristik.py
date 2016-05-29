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

def reduce(x):#löscht die ersten 3 und letzten 3 ziffern des arrays
    b = len(x)
    y = np.zeros(b-6)
    for i in range(3, b-3):
        y[i-3] =  x[i]
    return(y)

spannung, zaehlung = np.genfromtxt('daten/rohrcharakteristik.txt',unpack = 'True')
fehlerN = np.sqrt(zaehlung)/10
N = zaehlung/10
#print('Fehler N', fehlerN)

#Plot mit Fehlerbalken
plt.errorbar(spannung, N, yerr=fehlerN, fmt='x', label = 'Messwerte mit Fehlerbalken')
plt.plot(spannung, N, 'kx')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$N$')

#Ausgleichsrechnung
x_data = np.linspace(360, 670, 1000)
m, m_error, b, b_error = linregress(reduce(spannung), reduce(N))
plt.plot(x_data, m*x_data+b, 'r-', label = 'Ausgleichsgerade')

#Steigung in %
print('N(10) = ', N[10])
m_komplett = ufloat(m, m_error)
N_500 = ufloat(N[10], fehlerN[10])
steigung = (m_komplett*100)/N_500*100
print('m = ', m_komplett)
print('steigung in %= ',steigung)


plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/rohrcharakteristik.pdf')
