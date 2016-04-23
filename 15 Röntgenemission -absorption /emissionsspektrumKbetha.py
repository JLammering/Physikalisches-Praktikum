import matplotlib.pyplot as plt
import numpy as np

theta, Imp = np.genfromtxt('Daten/emissionsspektrumKbetha.txt', unpack = True)
plt.plot(theta, Imp, 'k.', label = r'Messwerte')

a, b, c = np.polyfit(theta, Imp, 2)
x = np.linspace(42.5, 46)
plt.plot(x, a*x**2 + b*x + c, 'r-', label = r'Ausgleichspolynom')

plt.grid()
plt.ylim(0,4000)
plt.legend(loc = 'best')
plt.savefig('build/emissionsspektrumKbetha.pdf')
