# Systematische Fehler einseitig eingespannter runder Stab
import matplotlib.pyplot as plt
import numpy as np

# Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab1einfach.txt', unpack = True)
d = 1/1000*(d1-d2)

# Plot der Messwerte:
L = 0.462
plt.plot(d, L*x**2 - x**3/3, 'k.',
label = r'Messwerte D gegen f(x) aufgetragen')

# Rest:
#plt.xlabel(r'$A/\si{\meter}$')
#plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('Stab1einfachFehler.pdf')
