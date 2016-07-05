import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

I,U = np.genfromtxt('Daten/c.txt',unpack= True)
U2,I2 = np.genfromtxt('Daten/c2.txt',unpack= True)

I2m = np.mean(I2)
N = 27
dI2 = np.sqrt(N/(N-1)*np.mean((I2-I2m)**2))
I2w = ufloat(I2m,dI2)

x = np.linspace(-23,23)
plt.plot(x,0*x+I2m,'r-', label = r'Mittelwert Gegenstrom')
plt.plot((0,0),(-0.3,8), 'b--', label = r'Bremsspannung')
plt.plot(I,U,'kx',label=r'Messwerte')

print('Mittelwert Ig:',I2w)

plt.legend(loc='best')
plt.ylim(-0.4, 7)
plt.xlim(-20,20)
plt.grid()
plt.xlabel(r'$U/\si{\volt}$')
plt.ylabel(r'$I/\si{\nano\ampere}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/c.pdf')
