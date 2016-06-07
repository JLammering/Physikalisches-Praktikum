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

#Daten2:
t2,I2 = np.genfromtxt('Daten/Rhodium2.txt',unpack='True')
t2 = t2*20

#Nullwert:
N0 = 195/900

#Anpassung Nullwert (20 s):
N0 = N0*20

I2 = I2 - N0

plt.errorbar(t2, I2, xerr=0, yerr=np.sqrt(I2) ,fmt='kx',label = r'Messwerte') #Messwerte

#lineare Regression:
m2,dm2,b2,db2 = linregress(t2,np.log(I2))
x = np.linspace(390,720)
plt.plot(x,np.exp(m2*x+b2),'r-',label = r'Ausgleichsfunktion')

B2 = ufloat(b2,db2)
N2 = unp.exp(B2)
M2 = ufloat(m2,dm2)
T2 = -np.log(2)/M2

print(
'Verschiebung:',B2,
'Vorfaktor:',N2,
'Steigung:',M2,
'Halbwertszeit:',T2,
'Messwerte mit Nulleffekt:',I2,
'Poisson-Fehler:',np.sqrt(I2)
)

plt.legend(loc='best')
plt.xlim(390,720)
plt.yscale('log')
plt.grid()
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.savefig('build/Rhodium2.pdf')
