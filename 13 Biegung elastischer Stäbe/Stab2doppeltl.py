# zweiseitig eingespannter quadratischer Stab Fit links
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

# Messwerte für Abstand, linksOhneGew, rechtsOhneGew, linksMitGew, rechtsMitGew:
x, dlog, drog, dlmg, drmg = np.genfromtxt('Stab2doppelt.txt', unpack = True)
x = x/100
dr = (dlog-dlmg)/1000
dl = (drog-drmg)/1000

dl = dl[::-1]
# Abstand von links gesehen:
xl = x
xr = 0.275 + x

# Gewicht, Kraft:
m = 4.7094
g = 9.81
F = m*g

# Trägheitsmoment, Durchmesser, Länge des Stabes:
L = 0.55
Du = ufloat(0.009968,0.000025)
I = Du**4/12

# Ausgleichsfunktionen für rechts und links:

def DL(xl, El):
    return F/(48*El*I.n)*(3*L**2*xl - 4*xl**3)

lparams, lcov = curve_fit(DL, xl, dl)

El_value = lparams
El_error = np.sqrt(np.diag(lcov))

a = np.linspace(0, 0.275)
plt.plot(a, 1000*DL(a,*lparams), 'r-', label = r'Ausgleichsfunktion')

print(El_value, El_error)

# Plot der Messwerte
plt.plot(xl,1000*dl,'k.', label = r'Messwerte')

# Rest:
plt.xlim(0,0.275)
plt.xlabel(r'$f(x)/\si{\meter}$')
plt.ylabel(r'$D/\si{\milli\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab2doppeltl.pdf')
