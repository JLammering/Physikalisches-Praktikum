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

I1 = I1 - N0
I2 = I2 - N0

#lineare Regression:
m2,dm2,b2,db2 = linregress(t2,np.log(I2)) #zweites Isotop(wichtig für die Differenz)

plt.plot(t1,I1,'kx')
I1 = I1 - np.exp(m2*t1+b2) #zweite e-Fkt wird abgezogen

#zweite lineare Regression
m1,dm1,b1,db1 = linregress(t1,np.log(I1))

x = np.linspace(0,700)
plt.plot(x,np.exp(m1*x+b1),'g-',label = r'kurze Ausgleichsfunktion')
plt.plot(x,np.exp(m2*x+b2),'b-',label = r'lange Ausgleichsfunktion')
plt.plot(x,np.exp(m1*x+b1)+np.exp(m2*x+b2),'k-',label = r'Summierte Ausgleichsfunktion')
plt.plot(t2,I2,'kx',label = r'Messwerte')
plt.plot((400,400),(1,1000),'r--', label = r'Grenze') # t*



B1 = ufloat(b1,db1)
M1 = ufloat(m1,dm1)
B2 = ufloat(b2,db2)
M2 = ufloat(m2,dm2)

tk = unp.exp(M1*400+B1)
tl = unp.exp(M2*400+B2)

print(
'tgrenze kurz:',tk,
'tgrenze lang:',tl
)

plt.legend(loc = 'best')
plt.xlabel(r't/\si{\second}')
plt.ylabel(r'P')
plt.grid()
plt.xlim(0,660)
plt.ylim(1,1000)
plt.yscale('log')
plt.savefig('build/RhodiumE.pdf')
