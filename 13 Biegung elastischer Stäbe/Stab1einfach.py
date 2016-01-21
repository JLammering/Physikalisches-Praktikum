#einseitig eingespannter runder Stab
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from scipy.optimize import curve_fit

# Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab1einfach.txt', unpack = True)
d = 1/1000*(d1-d2)

# Gewicht, Kraft:
m = 1.1831
g = 9.81
F = m*g

# Trägheitsmoment, Radius, Länge des Stabes:
L = 0.462
R = ufloat(0.01003,0.00005)*0.5
I = (np.pi*R**4)/3

# Plot der Messwerte:
plt.plot(x, d, 'k.')

# Abstandsfunktion und Plot:
def D(x, E):
    return F/(2*E*I.n) * (L*x**2-x**3/3)

params,cov = curve_fit(D, x, d)

a = np.linspace(0,0.5)
plt.plot(a, D(a,*params), 'b-', label = r'Ausgleichsfunktion')

# Elastizitätsmodul:
E_error = np.sqrt(np.diag(cov))
E_value = params
print(E_value, E_error)

# Rest:
#plt.xlabel(r'$A/\si{\meter}$')
#plt.ylabel(r'$D/\si{\meter}$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('Stab1einfach.pdf')


#gewichte eckig:
#e 0.5395
#d 4709.4

#e l=48.2 48.15 48.2
#d l=55cm
