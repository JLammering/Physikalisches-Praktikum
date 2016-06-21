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

#Grundwerte:
etaL1 = 1.875e-5
etaL2 = 1.881e-5
g = 9.81
rhoO = 886
rhoL = 1.164
d = ufloat(0.007625,0.000005)

#Daten:
U1, t01, tab1, tauf1 = np.genfromtxt('Daten/T1.txt',unpack = True)
U2, t02, tab2, tauf2 = np.genfromtxt('Daten/T2.txt',unpack = True)
U3, t03, tab3, tauf3 = np.genfromtxt('Daten/T3.txt',unpack = True)
U4, t04, tab4, tauf4 = np.genfromtxt('Daten/T4.txt',unpack = True)
U5, t05, tab5, tauf5 = np.genfromtxt('Daten/T5.txt',unpack = True)
U6, t06, tab6, tauf6 = np.genfromtxt('Daten/T6.txt',unpack = True)
U7, t07, tab7, tauf7 = np.genfromtxt('Daten/T7.txt',unpack = True)

#Mittelwerte:
tab1 = ufloat(np.mean(tab1),np.sqrt(tab1.size/(tab1.size-1)*np.mean((tab1 - np.mean(tab1))**2)))
tauf1 = ufloat(np.mean(tauf1),np.sqrt(tauf1.size/(tauf1.size-1)*np.mean((tauf1-np.mean(tauf1))**2)))

tab2 = ufloat(np.mean(tab2),np.sqrt(tab2.size/(tab2.size-1)*np.mean((tab2-np.mean(tab2))**2)))
tauf2 = ufloat(np.mean(tauf2),np.sqrt(tauf2.size/(tauf2.size-1)*np.mean((tauf2-np.mean(tauf2))**2)))

tab3 = ufloat(np.mean(tab3),np.sqrt(tab3.size/(tab3.size-1)*np.mean((tab3-np.mean(tab3))**2)))
tauf3 = ufloat(np.mean(tauf3),np.sqrt(tauf3.size/(tauf3.size-1)*np.mean((tauf3-np.mean(tauf3))**2)))

tab4 = ufloat(np.mean(tab4),np.sqrt(tab4.size/(tab4.size-1)*np.mean((tab4-np.mean(tab4))**2)))
tauf4 = ufloat(np.mean(tauf4),np.sqrt(tauf4.size/(tauf4.size-1)*np.mean((tauf4-np.mean(tauf4))**2)))

tab5 = ufloat(np.mean(tab5),np.sqrt(tab5.size/(tab5.size-1)*np.mean((tab5-np.mean(tab5))**2)))
tauf5 = ufloat(np.mean(tauf5),np.sqrt(tauf5.size/(tauf5.size-1)*np.mean((tauf5-np.mean(tauf5))**2)))

tab6 = ufloat(np.mean(tab6),np.sqrt(tab6.size/(tab6.size-1)*np.mean((tab6-np.mean(tab6))**2)))
tauf6 = ufloat(np.mean(tauf6),np.sqrt(tauf6.size/(tauf6.size-1)*np.mean((tauf6-np.mean(tauf6))**2)))

tauf7 = ufloat(np.mean(tauf7),np.sqrt(tauf7.size/(tauf7.size-1)*np.mean((tauf7-np.mean(tauf7))**2)))
tab7 = ufloat(np.mean(tab7),np.sqrt(tab7.size/(tab7.size-1)*np.mean((tab7-np.mean(tab7))**2)))

#Geschwindigkeiten:
v01   = 0.001/np.mean(t01)
vab1  = 0.001/tab1
vauf1 = 0.001/tauf1
ver1 = 2*np.mean(v01)/(vab1-vauf1)

v02   = 0.001/np.mean(t02)
vab2  = 0.001/tab2
vauf2 = 0.001/tauf2
ver2 = 2*np.mean(v02)/(vab2-vauf2)

v03   = 0.001/np.mean(t03)
vab3  = 0.001/tab3
vauf3 = 0.001/tauf3
ver3 = 2*np.mean(v03)/(vab3-vauf3)

v04   = 0.001/np.mean(t04)
vab4  = 0.001/tab4
vauf4 = 0.001/tauf4
ver4 = 2*np.mean(v04)/(vab4-vauf4)

v05   = 0.001/np.mean(t05)
vab5  = 0.001/tab5
vauf5 = 0.001/tauf5
ver5 = 2*np.mean(v05)/(vab5-vauf5)

v06   = 0.001/np.mean(t06)
vab6  = 0.001/tab6
vauf6 = 0.001/tauf6
ver6 = 2*np.mean(v06)/(vab6-vauf6)

v07   = 0.001/np.mean(t07)
vab7  = 0.001/tab7
vauf7 = 0.001/tauf7
ver7 = 2*np.mean(v07)/(vab7-vauf7)

#Radius:
r1 = unp.sqrt(9*etaL1*(vab1 - vauf1)/(4*g*(rhoO-rhoL)))
r2 = unp.sqrt(9*etaL1*(vab2 - vauf2)/(4*g*(rhoO-rhoL)))
r3 = unp.sqrt(9*etaL1*(vab3 - vauf3)/(4*g*(rhoO-rhoL)))
r4 = unp.sqrt(9*etaL1*(vab4 - vauf4)/(4*g*(rhoO-rhoL)))
r5 = unp.sqrt(9*etaL1*(vab5 - vauf5)/(4*g*(rhoO-rhoL)))
r6 = unp.sqrt(9*etaL2*(vab6 - vauf6)/(4*g*(rhoO-rhoL)))
r7 = unp.sqrt(9*etaL2*(vab7 - vauf7)/(4*g*(rhoO-rhoL)))

print(
#Zeiten1:',tab1, tauf1,
#Zeiten2:',tab2, tauf2,
#Zeiten3:',tab3, tauf3,
#Zeiten4:',tab4, tauf4,
#Zeiten5:',tab5, tauf5,
#Zeiten6:',tab6, tauf6,
#Zeiten7:',tab7, tauf7,
'Radius:', r1, r2, r3, r4, r5, r6, r7,
'Geschwindigkeiten:',
v01, vab1, vauf1, ver1,
v02, vab2, vauf2, ver2,
v03, vab3, vauf3, ver3,
v04, vab4, vauf4, ver4,
v05, vab5, vauf5, ver5,
v06, vab6, vauf6, ver6,
v07, vab7, vauf7, ver7,
'Verhältnis:', ver1, ver2, ver3,
ver4, ver5, ver6, ver7)

q1u = 3 * np.pi * etaL1 * d * (vab1+vauf1) * unp.sqrt(9*etaL1*(vab1-vauf1)/
(4*g*(rhoO-rhoL)))/np.mean(U1)

q2u = 3 * np.pi * etaL1 * d * (vab2+vauf2) * unp.sqrt(9*etaL1*(vab2-vauf2)/
(4*g*(rhoO-rhoL)))/np.mean(U2)

q3u = 3 * np.pi * etaL1 * d * (vab3+vauf3) * unp.sqrt(9*etaL1*(vab3-vauf3)/
(4*g*(rhoO-rhoL)))/np.mean(U3)

q4u = 3 * np.pi * etaL1 * d * (vab4+vauf4) * unp.sqrt(9*etaL1*(vab4-vauf4)/
(4*g*(rhoO-rhoL)))/np.mean(U4)

q5u = 3 * np.pi * etaL1 * d * (vab5+vauf5) * unp.sqrt(9*etaL1*(vab5-vauf5)/
(4*g*(rhoO-rhoL)))/np.mean(U5)

q6u = 3 * np.pi * etaL2 * d * (vab6+vauf6) * unp.sqrt(9*etaL2*(vab6-vauf6)/
(4*g*(rhoO-rhoL)))/np.mean(U6)

q7u = 3 * np.pi * etaL2 * d * (vab7+vauf7) * unp.sqrt(9*etaL2*(vab7-vauf7)/
(4*g*(rhoO-rhoL)))/np.mean(U7)

print('Ladungen:',q1u, q2u, q3u, q4u, q5u, q6u, q7u)

a = [3, 6, 2, 5, 6, 9]
qum = [4.5, 9.5, 3.5, 8.1, 10, 15]
que = [0.31, 1.9, 1.0, 0.7, 0.4, 0.4]

plt.errorbar(a,qum,xerr=0,yerr=que, fmt= 'kx', label = r'gewertete Ladungen')
plt.errorbar(2,3.4,xerr=0,yerr=1.2, fmt= 'rx', label = r'nicht gewertete Ladungen')
m,dm,b,db = linregress(a,qum)
x = np.linspace(0,10)
plt.plot(x, m*x+b, label=r'Ausgleichsgerade')
M = ufloat(m,dm)
B = ufloat(b,db)
F = ufloat(96485.3329,0.0006)
print('Steigung,Abschnitt', M,B,
'Avogadro:',F*10**(19)/M)

plt.legend(loc='best')
plt.xlabel(r'$gV$')
plt.ylabel(r'$q/\si{\coulomb}$')
plt.grid(True, linewidth=0.16)
plt.xlim(0,10)
plt.ylim(0,16)
plt.savefig('build/unkor.pdf')
