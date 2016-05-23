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
N0a = 195
N0b = 202
N0  = (N0a+N0b)/2
dN0 = np.sqrt((N0a-N0)**2 + (N0b-N0)**2)

#Anpassung Nullwert (20 s):
N0 = N0/45
dN0 = dN0/45

I2 = I2 - N0

plt.plot(t2, I2, 'kx',label = r'Messwerte') #Messwerte

#lineare Regression:
m2,dm2,b2,db2 = linregress(t2,np.log(I2))
x = np.linspace(390,700)
plt.plot(x,np.exp(m2*x+b2),'r-',label = r'Ausgleichsfunktion')

B2 = ufloat(b2,db2)
N2 = unp.exp(B2)
M2 = ufloat(m2,dm2)
T2 = -np.log(2)/M2

print(
'Verschiebung:',B2,
'Vorfaktor:',N2,
'Steigung:',M2,
'Halbwertszeit:',T2
)

plt.legend(loc='best')
plt.xlim(390,650)
plt.yscale('log')
plt.grid()
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.savefig('build/Rhodium2.pdf')
