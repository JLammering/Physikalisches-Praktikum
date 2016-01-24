# Systematische Fehler einseitig eingespannter runder Stab
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab1einfach.txt', unpack = True)
d = (d1-d2)/1000

# Plot der Messwerte D1e gegen f1(x):
L = 0.462

def f1(x):
    return L*x**2 - x**3/3

plt.plot(f1(x), d, 'k.', label = r'Messwerte')

# Ausgleichsgerade:
a, b, rv, pv, err = linregress(f1(x), d)
u = np.linspace(0,0.07)
plt.plot(u, a*u + b,'r-', label = r'Ausgleichsgerade')
print('Steigung, Fehler, Abweichung:', a, err, err/a)

# Rest:
plt.xlabel(r'$f(x)/\si{\cubic\meter}$')
plt.ylabel(r'$D/\si{\meter}$')
plt.xlim(0,0.07)
plt.ylim(0,0.004)
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab1einfachFehler.pdf')
