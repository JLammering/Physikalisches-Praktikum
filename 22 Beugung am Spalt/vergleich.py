import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

def doppel(phi, A_0, s, b):
    return (A_0 * (np.cos((np.pi*s*np.sin(phi))/lamda))**2 *(lamda/(np.pi*b*np.sin(phi)))**2 * (np.sin(np.pi*b*np.sin(phi)/lamda))**2)

def einzel(phi, A_0, b):
    return (A_0**2 * b**2 *(lamda/(np.pi*b*np.sin(phi)))**2 * (np.sin(np.pi*b*np.sin(phi)/lamda))**2)

L = 1#m
lamda = 633e-9
#Parameter einzelspalte
A_0_1 = 7.513
b_1 = 7.496e-5
A_0_2 = 9.271
b_2 = 0.1457e-3
A_0_3 = 12.092
b_3 = 0.3608e-3
#Parameter doppelspalt
A_0_doppel = 3.681e-6
s_doppel = 0.483e-3
b_doppel = 0.1011e-3


x_plot = np.linspace(-15e-3, 15e-3, 10000)
phi_plot = x_plot/L
plt.plot(phi_plot, einzel(phi_plot, A_0_1, b_1)*1e6, 'b-', label = 'Einfachspalt 1')
plt.plot(phi_plot, einzel(phi_plot, A_0_2, b_2)*1e6, 'r-', label = 'Einfachspalt 2')
plt.plot(phi_plot, einzel(phi_plot, A_0_3, b_3)*1e6, 'g-', label = 'Einfachspalt 3')
plt.plot(phi_plot, doppel(phi_plot, A_0_doppel, s_doppel, b_doppel)*1e6, 'm-', label = 'Doppelspalt')

plt.ylim(0,5)

plt.xlabel(r'$\varphi \:/\: \si{\radian}$')
plt.ylabel(r'$(I-I_0) \:/\: \si{\micro\ampere}$')


plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/vergleich.pdf')
plt.show()
