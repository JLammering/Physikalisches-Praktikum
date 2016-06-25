import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

U, I1, I2, I3, I4, I5 = np.genfromtxt('daten/kennlinien.txt',unpack = 'True')

plt.plot(U, I1, 'kx', label = 'Messwerte $I_1$')
plt.plot(U, I2, 'gx', label = 'Messwerte $I_2$')
plt.plot(U, I3, 'yx', label = 'Messwerte $I_3$')
plt.plot(U, I4, 'cx', label = 'Messwerte $I_4$')
plt.plot(U, I5, 'rx', label = 'Messwerte $I_5$')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$I \:/\: \si{\milli\ampere}$')
plt.xlim(0, 260)

plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/kennlinien.pdf')
