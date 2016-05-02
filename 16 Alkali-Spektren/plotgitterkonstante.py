import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Messwerte plotten
lamda, phi = np.genfromtxt('Daten/gitterkonstante.txt', unpack=True)
x = lamda
phi = 305.3 - phi #relativ zur 0. Ordnung
print('phi in °= ',phi)
phi *= (1/360)*2*np.pi #in rad umrechnen
print('phi in rad = ',phi)
y = np.sin(phi)

plt.plot(x, y, 'kx', label='Messwerte') #sin(phi) in Abhängigkeit von lambda
plt.xlabel(r'$\lambda \:/\: \si{\nano\meter}$')
plt.ylabel(r'$sin(\phi) \:/\: 1$')
plt.legend(loc='best')

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

m, m_error, B, B_error =linregress(x, y) #m ist Steigung B ist y-Achsenab
m = ufloat(m, m_error)
g = 1/m

#Ausgleichsgerade plotten

x_plot = np.linspace(400, 750, 1000)
plt.plot(x_plot, m.n * x_plot + B, 'b-', label = 'Ausgleichsgerade')

np.savetxt('build/gitterkonstante.txt', np.column_stack([m.n, m.s, g.n, g.s, B, B_error]),
header="Steigung, Fehler Steigung, gitterkonstante, Fehler gitterkonstante, y-Achsenab, Fehler y-Achsenab")


# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotgitterkonstante.pdf')
