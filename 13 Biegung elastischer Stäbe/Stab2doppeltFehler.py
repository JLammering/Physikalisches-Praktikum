# systematischer Fehler zweiseitig eingespannter quadratischer Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.stats import linregress
from scipy.optimize import curve_fit

# Messwerte für Abstand, linksOhneGew, rechtsOhneGew, linksMitGew, rechtsMitGew:
x, dlog, drog, dlmg, drmg = np.genfromtxt('Stab2doppelt.txt', unpack = True)
x = x/100
dl = (dlog-dlmg)/1000
dr = (drog-drmg)/1000
dl = dl[::-1]
dr = dr[::-1]

# Plot der Messwerte D1e gegen f1(x):
L = 0.55
def f2(x):
    return 3*(L**2)*x - 4*x**3

#links:
plt.plot(dl, f2(x), 'k.', label = r'Messwerte links')

#rechts:
plt.plot(dr, f2(x), 'r.', label = r'Messwerte rechts')

# Ausgleichsgerade:
def g(x, a):
    return a*x

lpar, lcov = curve_fit(g, dl, f2(x))
rpar, rcov = curve_fit(g, dr, f2(x))
u = np.linspace(0,0.00145)
plt.plot(u, g(u,*lpar),'k-', label = r'Ausgleichsgerade links')
plt.plot(u, g(u,*rpar),'r-', label = r'Ausgleichsgerade rechts')

lerr = np.sqrt(np.diag(lcov))
rerr = np.sqrt(np.diag(rcov))

print(
'Steigung,Fehler links:',lpar, lerr,
'Steigung,Fehler rechts',lpar, rerr
)

# Rest:
plt.xlim(0, 0.00145)
plt.xlabel(r'$f(x)/\si{\meter}$')
plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab2doppeltFehler.pdf')
