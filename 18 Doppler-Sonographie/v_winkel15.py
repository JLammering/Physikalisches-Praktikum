import matplotlib.pyplot as plt
import numpy as np

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

nu_0 = 2e6#hertz

alpha = np.array([80.06, 70.53, 54.74])
alpha = (alpha/360)*2*np.pi
c=1800#vermutlich die schallgeschwindigkeit in der Flüssigkeit

d_winkel15, delta_nuwinkel15= np.genfromtxt('daten/v_winkel15.txt',unpack = 'True')

#winkel 15
v_winkel15 = (delta_nuwinkel15/(2*nu_0*np.cos(alpha[0])))*c
#print('v_winkel15 = ', v_winkel15)
x = v_winkel15
y =  delta_nuwinkel15/np.cos(alpha[0])

m, m_err, y_achs, y_errachs = linregress(x, y)
#print('m= ',m, '2 nu_0/c =', 2*nu_0/c, 'm_err= ',m_err)

np.savetxt('build/linv_winkel15.txt', np.column_stack([m, m_err, y_achs, y_errachs]),
header="Steigung, Fehler Steigung, y-Achsenab, Fehler y-Achsenab")
np.savetxt('build/v_winkel15.txt', np.column_stack([v_winkel15]),
header="v_winkel15")

x_plot = np.linspace(0.0, 2.0, 1000)

plt.plot(x, y,'kx', label='Messwerte')
plt.plot(x_plot, m*x_plot+y_achs, 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$v \:/\: \si{\meter\per\second}$')
plt.ylabel(r'$\Delta \nu/\cos(\alpha) \:/\: \si{\hertz}/\cos(\si{\radian})$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotvwinkel15.pdf')
