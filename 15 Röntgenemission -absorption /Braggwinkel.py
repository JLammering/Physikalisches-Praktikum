import matplotlib.pyplot as plt
import numpy as np

E = np.array([9.65, 11.10, 13.47, 15.20, 16.11, 18.00, 18.98])

dLiF = 201.4 * 10**(-12)
h = 6.6261 * 10**(-34)
c = 299792458
f = E/h /(1000*1.6022*10**-19)
lambda = c/f

theta = np.arcsin(n*lambda/(2*dLiF))

print(theta)
