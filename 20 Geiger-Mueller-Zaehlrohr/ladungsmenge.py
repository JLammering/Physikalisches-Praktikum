import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

e = ufloat(1.6021766208e-19, 0.0000000098e-19)

spannung1, stromstaerke = np.genfromtxt('daten/ladungsmenge.txt',unpack = 'True')
spannung2, zaehlung = np.genfromtxt('daten/rohrcharakteristik.txt',unpack = 'True')
fehlerN = np.sqrt(zaehlung)/10
N = zaehlung/10
Nerr = unp.uarray(N, fehlerN)
I = unp.uarray(stromstaerke*10**(-6),0.05*10**(-6))

delQ = (I/Nerr)/e
print(I,Nerr,delQ)

np.savetxt('build/ladungsmengeergebnisse.txt', np.column_stack([spannung1, unp.nominal_values(I), unp.nominal_values(delQ), unp.std_devs(delQ)]),
header="Spannung, stromstaerke, Ladung, Fehler Ladung")
