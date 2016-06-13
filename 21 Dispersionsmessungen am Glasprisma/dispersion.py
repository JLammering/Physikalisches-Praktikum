import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

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

#Innenwinkel des Prismas:
phil = 320
phir = 72.3

phi = (360-phil+phir)/2

#Daten:
lamda, eta = np.genfromtxt('Daten/Datenb.txt',unpack=True)
n = np.sin((eta+phi)*2*np.pi/720)/np.sin(phi*2*np.pi/720)
n = n**2
nausgabe = unp.sin((eta+phi)*2*np.pi/720)/unp.sin(phi*2*np.pi/720)
plt.plot(lamda,n,'kx', label = r'Messwerte')

lc = 656
ld = 589
lf = 486

#erste Regression:
lamda1 = 1/(lamda**2)

m1,dm1,b1,db1 = linregress(lamda1,n)

s1 = 7/5 * np.mean((n-b1-m1*lamda1)**2)  #Summe Abweichungsquadrate:

x = np.linspace(400,800)
plt.plot(x,m1*(1/(x**2)) + b1,'r-',label = r'Ausgleichsfunktion')

#zweite Regression
lamda2 = lamda**2

m2,dm2,b2,db2 = linregress(lamda2,n)

s2 = 7/5 * np.mean((n-b2-m2*lamda2)**2)  #Summe Abweichungsquadrate:

x = np.linspace(400,800)
#plt.plot(x,m2*x**2 + b2,'b-')

#Endwerte:
A1 = ufloat(b1,db1)
A2 = ufloat(m1,dm1)

B1 = ufloat(b2,db2)
B2 = ufloat(m2,dm2)

#Abbesche Zahl:
nc = unp.sqrt(A1 + A2/((lc)**2))
nd = unp.sqrt(A1 + A2/((ld)**2))
nf = unp.sqrt(A1 + A2/((lf)**2))
nu = (nd-1)/(nf-nc)

#Auflösungsvermögen:
Ac = 0.03 * (-A2)/(lc**3) * (unp.sqrt(A1+A2/(lc**2)))**(-1)
Af = 0.03 * (-A2)/(lf**3) * (unp.sqrt(A1+A2/(lf**2)))**(-1)

#Absorptionsstelle:
la1 = unp.sqrt(A2/(A1-1))

print(
'A1,A2:',A1,A2,
'B1,B2:',B1,B2,
'phi:',phi,
'Funktionswerte für Abbe:', nc, nd, nf,
'AbbescheZahl:',nu,
'Abweichungsquadrate:',s1,s2,
'Auflösungsvermögen:',Ac,Af,
'Brechungsindize:',nausgabe,
'Absorptionsstelle:',la1
)

plt.xlabel(r'$\lambda$')
plt.ylabel(r'$n^2(\lambda)$')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/dispersion.pdf')
