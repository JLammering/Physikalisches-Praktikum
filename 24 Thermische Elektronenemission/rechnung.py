import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

e = ufloat(1.6021766208e-19, 0.0000000098e-19)#C
k = ufloat(1.38064852e-23, 0.00000079e-23)#J/K
h = ufloat(6.626070040e-34, 0.000000081e-34)#J s
f = 0.35#cm^2
m0 = ufloat(9.10938356e-31, 0.00000011e-31)#kg

def mittelwert(sigma):
    l = len(sigma)
    sum = ufloat(0, 0)
    for i in range(0, l):
        sum += sigma[i]
    return (1/l)*sum

#Kathodentemperatur
Ih = np.array([2.5, 2.4, 2.3, 2.2, 2.1])#A
Uh = np.array([6, 6, 5.5, 5, 5])#V
Nzu = Ih*Uh#W
N_WL = 1#W
print('Nzu = ', Nzu)


sigma = 5.7e-12 #W/cm^2K^4
f = 0.35e-4#cm^2
eta = 0.28

T = np.sqrt(np.sqrt((Nzu - N_WL)/(f*sigma*eta)))
print('T = ', T)

#Austrittsarbeit
I_S = np.array([2.6, 1.5, 0.76, 0.35])
I_S *= 1e-3
T = np.array([2213.1, 2137, 2057, 2030.7])

phi = -(k*T) * unp.log((I_S * h**3)/ (4 * np.pi * f * e * m0 * k**2 * T**2))
phieV = phi/e
print('phieV = ',phieV)

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)*100

phimittel = np.mean(unp.nominal_values(phieV))
phistaabw = np.std(unp.nominal_values(phieV))
print('phimittel = ', phimittel,'±', phistaabw)


print('Delta phi = ', abweichung(phimittel, 4.54))
