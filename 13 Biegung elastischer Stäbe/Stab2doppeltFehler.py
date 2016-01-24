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
plt.plot(f2(x), dl, 'k.', label = r'Messwerte links')

#rechts:
plt.plot(f2(x), dr, 'r.', label = r'Messwerte rechts')

# Ausgleichsgerade:
def g(x, a):
    return a*x

lpar, lcov = curve_fit(g, f2(x), dl)
rpar, rcov = curve_fit(g, f2(x), dr)
u = np.linspace(0,0.167)
plt.plot(u, g(u,*lpar),'k-', label = r'Ausgleichsgerade links')
plt.plot(u, g(u,*rpar),'r-', label = r'Ausgleichsgerade rechts')

lerr = np.sqrt(np.diag(lcov))
rerr = np.sqrt(np.diag(rcov))

print(
'Steigung,Fehler,Abweichung links:',lpar, lerr, lerr/lpar,
'Steigung,Fehler,Abweichung rechts',rpar, rerr, rerr/rpar
)

# Rest:
plt.xlim(0, 0.167)
plt.ylim(0, 0.0016)
plt.xlabel(r'$f(x)/\si{\cubic\meter}$')
plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('build/Stab2doppeltFehler.pdf')
