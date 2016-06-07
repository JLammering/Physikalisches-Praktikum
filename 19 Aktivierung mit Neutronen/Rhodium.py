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

#Daten1:
t1, I1 = np.genfromtxt('Daten/Rhodium.txt',unpack = 'True')
t1 = t1*20

#Daten2:
t2, I2 = np.genfromtxt('Daten/Rhodium2.txt',unpack = 'True')
t2 = t2*20

#Nullwert:
N0  = 195/900

#Anpassung Nullwert (20 s):
N0 = N0*20

I1 = I1 - N0
I2 = I2 - N0

u = I1

#lineare Regression:
m2,dm2,b2,db2 = linregress(t2,np.log(I2)) #zweites Isotop(wichtig für die Differenz)

I1 = I1 - np.exp(m2*t1+b2) #zweite e-Fkt wird abgezogen

#zweite lineare Regression
m1,dm1,b1,db1 = linregress(t1,np.log(I1))
x = np.linspace(0,400)

plt.plot(x,np.exp(m1*x+b1),'r-', label = r'Ausgleichsfunktion') #Regression
plt.errorbar(t1, I1, xerr = 0, yerr = np.sqrt(I1), fmt = 'kx', label = r'Messwerte') #Messwerte

B1 = ufloat(b1,db1)
N1 = unp.exp(B1)
M1 = ufloat(m1,dm1)
T1 = -np.log(2)/M1

I1 = u
tz = np.array([340, 360, 380])
Iz = np.array([36, 36, 40])
Iz = Iz-N0

print(
'Verschiebung:',B1,
'Vorfaktor:',N1,
'Steigung:',M1,
'Halbwertszeit T1:',T1,
'Messwerte mit Nulleffekt:',I1,Iz,
'Poisson-Fehler:',np.sqrt(I1),np.sqrt(Iz)
)

plt.grid()
plt.legend(loc='best')
plt.xlim(0,350)
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.yscale('log')
plt.savefig('build/Rhodium.pdf')
