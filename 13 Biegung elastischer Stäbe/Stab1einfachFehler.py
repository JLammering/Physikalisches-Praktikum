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

plt.plot(d, f1(x), 'k.', label = r'Messwerte')

# Ausgleichsgerade:
a, b, rv, pv, err = linregress(d, f1(x))
u = np.linspace(0,0.0039)
plt.plot(u, a*u + b,'r-', label = r'Ausgleichsgerade')
print('Fehler der Ausgleichsgerade:', rv)

# Rest:
plt.xlabel(r'$f(x)/\si{\meter}$')
plt.ylabel(r'$D/\si{\meter}$')
plt.xlim(0,0.0039)
plt.ylim(0,0.08)
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab1einfachFehler.pdf')
