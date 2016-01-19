import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def feldst(I):
    return 4*np.pi*(10**-7)*(8*I*80)/(np.sqrt(125)*0.072)*1000

#5 Punkte plotten
#1. bei 0.5 A
T05 = np.genfromtxt('Daten/daten05A.txt', unpack = True)
T_gem05 = np.mean(T05)
B05 = feldst(0.5)
momentwerteT = [1/T_gem05**2]
momentwerteB = [B05]
#errX = np.std(T)
#errY = 0
#plt.errorbar(1/T_gem**2 + errX, B + errY, xerr = errX, yerr = errY, fmt ='o', label ='Messwerte')

#2. bei 1 A
T1 = np.genfromtxt('Daten/daten1A.txt', unpack = True)
T_gem1 = np.mean(T1)
B1 = feldst(1)
momentwerteT.append(1/T_gem1**2)
momentwerteB.append(B1)

#3. bei 1.5 A
T15 = np.genfromtxt('Daten/daten15A.txt', unpack = True)
T_gem15 = np.mean(T15)
B15 = feldst(1.5)
momentwerteT.append(1/T_gem15**2)
momentwerteB.append(B15)

#4. bei 2 A
T2 = np.genfromtxt('Daten/daten2A.txt', unpack = True)
T_gem2 = np.mean(T2)
B2 = feldst(2)
momentwerteT.append(1/T_gem2**2)
momentwerteB.append(B2)

#5. bei 2.5 A
T25 = np.genfromtxt('Daten/daten25A.txt', unpack = True)
T_gem25 = np.mean(T25)
B25 = feldst(2.5)
momentwerteT.append(1/T_gem25**2)
momentwerteB.append(B25)

#plotten der Messwerte
plt.plot(momentwerteB, momentwerteT, 'rx', label = 'Messwerte')



#Ausgleichsgerade
slope, intercept, r_value, p_value, std_err = linregress(momentwerteB, momentwerteT)
a = np.linspace(0, 3, 1000)
plt.plot(a, slope*a + intercept, 'b-', label = r'$Ausgleichsgerade$')

#verschönern
plt.ylabel(r'$1/T_m^2\: / \: 1/\si{\square\second}$')
plt.xlabel(r'$B\:/\: \si{\milli\tesla}$')
plt.ylim(0, 0.02)
plt.xlim(0, 3)
plt.legend(loc = 'best')

#speichern
np.savetxt('build/momentwerte.txt', np.column_stack([momentwerteT, momentwerteB]), header = "1/T^2 , B ")
np.savetxt('build/momentausgleich.txt', np.column_stack([slope, intercept, r_value, std_err]), header = "slope, intercept, r_value, std_err ")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/momentplot.pdf')
