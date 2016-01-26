# Große Kugel Temperaturabhängigkeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

#Radius, Masse Werte:
D, M = np.genfromtxt('datendichtgr.txt', unpack = True)
M = M*10**(-3)
R = 0.5*D*10**(-3)

#Mittelwert und Fehler:
a = np.mean(R)
m = np.mean(M)

z = (R-a)**2
w = np.mean(z)*4/3
print('Radius-abweichung vom Mittelwert:', np.sqrt(w))

r = ufloat(a, np.sqrt(w))

V = 4/3 * np.pi * r**3

#Dichte:
p = m/V
print('Dichte:', p, 'Masse:', m, 'Radius:', r,'Volumen:',V)
P = 998.2

#Temperatur, Zeit Werte:
T, t = np.genfromtxt('datentemp.txt', unpack=True)
T = T+273.15

#p ohne Abweichung:
poa = 3*m/(4*np.pi*a**3)

#Viskosität:
K = 1.03e-08
n = K*(poa-P)*t

def f(T, A, B):
    return A*np.exp(B/T)

params, cov = curve_fit(f, T, n)

errors = np.sqrt(np.diag(cov))
print('Parameter A und B:', *params)
print('Fehler vom CurveFit:', errors)
print('Tabellenwerte:',
'Eta:', n*1000,
'ln(Eta):', np.log(n),
'1/T:', 1/T)

plt.plot(1/T, np.log(n), 'kx', label = r'Messwerte')
T = np.linspace(280, 350,1000)

1000*f(293.15, *params)*404.06

print('20', f(293.15, *params)*1000, 1002.0/1000,
100*(1-(1/(1000*f(293.15, *params))*1.002)))
print('30', f(303.15, *params)*1000, 797.68/1000,
100*(1-(1/(1000*f(303.15, *params))*0.79768)))
print('40', f(313.15, *params)*1000, 653.25/1000,
100*(1-(1/(1000*f(313.15, *params))*0.65325)))
print('50:', f(323.15, *params)*1000, 547.08/1000,
100*(1-(1/(1000*f(323.15, *params))*0.54708)))
print('60', f(333.15, *params)*1000, 466.59/1000,
100*(1-(1/(1000*f(333.15, *params))*0.46659)))
print('70', f(343.15, *params)*1000, 404.06/1000,
100*(1-(1/(1000*f(343.15, *params))*0.40406)))

plt.plot(1/T, np.log(f(T, *params)), 'r-', label = r'Ausgleichsgerade')

plt.xlabel(r'$(1/T)/\si{\kelvin}^{-1}$')
plt.ylabel(r'$ln(\eta/o)$')
plt.legend(loc = 'best')
plt.grid()
plt.xlim(0.0029, 0.0035)
plt.savefig('build/plotandrat.pdf')
