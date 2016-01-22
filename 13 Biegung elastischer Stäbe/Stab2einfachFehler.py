#Systematische Fehler einseitig eingespannter quadratischer Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

#Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab2einfach.txt', unpack = True)
d = (d1-d2)/1000
x = x/100

#Plot der Messwerte:
L = ufloat(0.48183,0.00025)
plt.plot(d, L.n*x**2 - x**3/3, 'k.',
label = r'Messwerte D gegen f(x) aufgetragen')

#Rest:
#plt.xlabel(r'$A/\si{\meter}$')
#plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('Stab2einfachFehler.pdf')
