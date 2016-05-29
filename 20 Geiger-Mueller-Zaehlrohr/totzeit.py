import numpy as np
from uncertainties import ufloat


#10s
N1mess = 5243
N2mess = 4477
N12mess = 9464
N1 = ufloat(N1mess/10, np.sqrt(N1mess)/10)
N2 = ufloat(N2mess/10, np.sqrt(N2mess)/10)
N12 = ufloat(N12mess/10, np.sqrt(N12mess)/10)

T10 = (N1 + N2 - N12)/(2*N1*N2)
print('Messung bei 10s: ')
print('N1 = ', N1, 'N2 = ',N2, 'N12 = ',N12, 'T10 = ',T10)

#60s
N1mess = 24076
N2mess = 21677
N12mess = 44506
N1 = ufloat(N1mess/60, np.sqrt(N1mess)/60)
N2 = ufloat(N2mess/60, np.sqrt(N2mess)/60)
N12 = ufloat(N12mess/60, np.sqrt(N12mess)/60)

T60 = (N1 + N2 - N12)/(2*N1*N2)
print('Messung bei 60s: ')
print('N1 = ', N1, 'N2 = ',N2, 'N12 = ',N12, 'T60 = ',T60)

#Mittelwert
T = (1/2)*(T10+T60)
print('T = ',T)
