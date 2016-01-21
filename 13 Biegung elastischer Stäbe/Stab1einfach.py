#einseitig eingespannter runder Stab
import matplotlib.pyplot as plt
import numpy as np

# Messwerte Abstand, ohneGewicht, mitGewicht:
x, d1, d2 = np.genfromtxt('Stab1einfach.txt', unpack = True)
d = d1-d2

# Gewicht, Kraft, Länge des Stabes:
m = 1.1831
g = 9.81
F = m*g
L = 46.2

# Abstandsfunktion:
def D(x, E):
    return F/(2*E) * (L*x**2-x**3/3)


gewichte eckig:
e 0.5395
d 4709.4

e l=48.2 48.15 48.2
d l=55cm
