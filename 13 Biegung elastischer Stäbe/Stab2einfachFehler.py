#Systematische Fehler einseitig eingespannter quadratischer Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.stats import linregress


#Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab2einfach.txt', unpack = True)
d = (d1-d2)/1000
x = x/100

#Plot der Messwerte:
L = ufloat(0.48183,0.00025)

def f1(x):
    return L.n*x**2 - x**3/3

plt.plot(f1(x), d, 'k.', label = r'Messwerte')

# Ausgleichsgerade:
a, b, rv, pv, err = linregress(f1(x), d)
u = np.linspace(0,0.07)
plt.plot(u, a*u + b,'r-', label = r'Ausgleichsgerade')
print('Steigung, Fehler, Abweichung:', a, err, err/a)

#Rest:
plt.xlim(0, 0.07)
plt.ylim(0,0.004)
plt.xlabel(r'$f(x)/\si{\cubic\meter}$')
plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab2einfachFehler.pdf')
