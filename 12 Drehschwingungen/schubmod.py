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
