import matplotlib.pyplot as plt
import numpy as np

theta, Imp = np.genfromtxt('Daten/emissionsspektrumKalpha.txt', unpack = True)
plt.plot(theta, Imp, 'k.', label = r'Messwerte')

a, b, c = np.polyfit(theta, Imp, 2)
x = np.linspace(38, 41)
plt.plot(x, a*x**2 + b*x + c, 'r-', label = r'Ausgleichspolynom')
hochpunktx = -b/(2*a)
hochpunkty = a*hochpunktx**2 + b*hochpunktx + c
halbwerty = hochpunkty/2
p = b/a
q = (c-halbwerty)/a
halbwertx1 = -p/2 + np.sqrt((p/2)**2-q)
halbwertx2 = -p/2 - np.sqrt((p/2)**2-q)
halbwertsbreite = halbwertx1 - halbwertx2

plt.plot(x, halbwerty*x**0, 'b-', label = r'Halbwert')

plt.plot(38.4, 122.0, 'k.')
plt.plot(40.8, 158.0, 'k.')

print("Hochpunkt(x,y):", hochpunktx, hochpunkty)
print("Halbwerte(y,x1,x2)", halbwerty, halbwertx1, halbwertx2)
print("Halbwertsbreite:", halbwertsbreite)
plt.grid()
plt.ylim(0,1300)
plt.legend(loc = 'best')
plt.savefig('build/emissionsspektrumKalpha.pdf')
