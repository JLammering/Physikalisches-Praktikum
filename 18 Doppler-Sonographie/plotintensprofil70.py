import matplotlib.pyplot as plt
import numpy as np

nu_0 = 2e6#hertz

alpha = np.array([80.06, 70.53, 54.74])
alpha = (alpha/360)*2*np.pi
c=1800#vermutlich die schallgeschwindigkeit in der Flüssigkeit

depth, deltanuv70, intens70 = np.genfromtxt('daten/stroemungsprofil70.txt',unpack = 'True')

#v_70 = (deltanuv70/(2*nu_0*np.cos(alpha[0])))*c

plt.plot(depth, intens70,'kx', label='Messwerte')
plt.xlabel(r'$b \:/\: \si{\micro\second}$')
plt.ylabel(r'$I \:/\: 10^3\si{\squared\volt\per\second}$')
plt.xlim(3, 21)
plt.ylim(0, 20000)
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotintensprofil70.pdf')
