# zweiseitig eingespannter quadratischer Stab
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
plt.plot(a, DL(a,*lparams), 'r-')

print(El_value, El_error)
def DR(xr, Er):
    return F/(48*Er*I.n)*(4*xr**3 - 12*L*xr**2 + 9*L**2*xr - L**3)

rparams, rcov = curve_fit(DR, xr, dr)
Er_value = rparams
Er_error = np.sqrt(np.diag(rcov))

a = np.linspace(0.275, 0.55)
plt.plot(a, DR(a,*rparams), 'r-')

print(Er_value, Er_error)

# Plot der Messwerte
plt.plot(xl,dl,'k.')
plt.plot(xr,dr,'r.')

plt.savefig('Stab2doppelt.pdf')
