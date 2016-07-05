import matplotlib.pyplot as plt
import numpy as np

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

I,U = np.genfromtxt('Daten/gruen.txt',unpack=True)
I = np.sqrt(I)

plt.plot(I,U,'kx',label = r'Messwerte')
m, dm, b, db = linregress(I,U)
x = np.linspace(0,0.8)
plt.plot(x, m*x + b, 'r-', label=r'Ausgleichsgerade')

print('Steigung:',m,dm,
'Abschnitt:',b,db)

plt.xlabel(r'$\sqrt{I/\si{\ampere}}$')
plt.ylabel(r'$U/\si{\volt}$')
plt.ylim(0,0.5)
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/gruen.pdf')
