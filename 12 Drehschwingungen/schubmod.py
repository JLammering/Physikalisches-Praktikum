import numpy as np
from uncertainties import ufloat

T = np.genfromtxt('Daten/datenvertikal.txt', unpack = True)
T_gem = ufloat(np.mean(T), np.std(T))
print('T_gem = ', T_gem)

m_k = ufloat(0.5883, 0.0004*0.5883)
print('m_k = ', m_k)

L = np.array([0.615 + 0.042, 0.615 + 0.043, 0.616 + 0.042])
L_gem = ufloat(np.mean(L), np.std(L))
print('L_gem = ', L_gem)

R = np.array([0.202e-3/2, 0.201e-3/2, 0.203e-3/2, 0.200e-3/2, 0.201e-3/2])
R_gem = ufloat(np.mean(R), np.std(R))
print('R_gem = ', R_gem)

R_k = ufloat(51.03e-3/2, 51.03e-3/2*0.0004)
print('R_k = ', R_k)

G = (16/5)*np.pi*(m_k*(R_k**2)*L_gem)/((T_gem**2)*(R_gem**4))
print('')
print('G = ', G)

print('')
E = 21e+10
mu = (E/2*G)-1
print('mu = ',mu)
Q = E/(3*(1-2*mu))
print('Q = ', Q)

thetakugel = (2/5)*m_k*R_k**2
print('')
print('thetakugel = ', thetakugel)
thetahalt = 22.5e-7
thetainsg = thetakugel + thetahalt
print('thetainsg = ', thetainsg)

print('magnetisches Moment')
a = ufloat(6.33, 0.06)
m = a*np.pi**2*thetainsg
print('m = ', m)

print('Erdmagnetfeld:')
T_hori = np.genfromtxt('Daten/datenhorizontal.txt', unpack = True)
T_horigem = ufloat(np.mean(T_hori), np.std(T_hori))
diff = T_horigem-T_gem
print('diff = ', diff)
T_horigem = T_gem - diff 
print('T_horigem = ', T_horigem)

D = (np.pi*G*R_gem**4)/(2*L_gem)
print('D = ', D)

B = (4*np.pi**2*thetainsg)/(m*T_horigem**2) - D/m
print('B = ', B)
