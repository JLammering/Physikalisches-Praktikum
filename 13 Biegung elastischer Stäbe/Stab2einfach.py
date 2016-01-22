#einseitig eingespannter quadratischer Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

# Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab2einfach.txt', unpack = True)
d = (d1-d2)/1000
x = x/100

# Gewicht, Kraft:
m = 0.5395
g = 9.81
F = m*g

# Trägheitsmoment, Durchmesser, Länge des Stabes:
L = ufloat(0.48183,0.00025)
Du = ufloat(0.009968,0.000025)
I = Du**4/12

# Plot der Messwerte:
plt.plot(x, d, 'k.')

# Abstandsfunktion und Plot:
def D(x, E):
    return F/(2*E*I.n) * (L.n*x**2-x**3/3)

params,cov = curve_fit(D, x, d)

a = np.linspace(0,0.5)
plt.plot(a, D(a,*params), 'b-', label = r'Ausgleichsfunktion')

# Elastizitätsmodul:
E_error = np.sqrt(np.diag(cov))
E_value = params
print(
'quad1:'
'Masse:', m,
'Kraft:', F,
'T-Moment:', I,
'E-Modul:', E_value, E_error
)

# Rest:
#plt.xlabel(r'$A/\si{\meter}$')
#plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('Stab2einfach.pdf')
