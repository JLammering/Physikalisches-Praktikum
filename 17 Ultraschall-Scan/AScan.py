import matplotlib.pyplot as plt
import numpy as np

#Schallgeschwindigkeit in Acryl:
c = 2730

#Höhe des Blocks:
h = 8.04

#Daten:
A1,LitD = np.genfromtxt('Daten/AScan1.txt',unpack = 'True')
A2,Lit2 = np.genfromtxt('Daten/AScan2.txt',unpack = 'True')

#Laufzeitkorrektur:
A1 = A1 - 0.5
A2 = A2 - 0.5

#Umrechnung in Sekunden:
A1 = A1 * 10**(-6)
A2 = A2 * 10**(-6)

#Berechnung der Strecke:
S1 = 100 * 0.5 * c * A1
S2 = 100 * 0.5 * c * A2

#Tiefe der Störstellen:
print('Tiefe der Störstellen[cm]:',S1,S2)

#Dicke der Störstellen:
D = h - S1 - S2
print('Dicke der Störstellen[cm]:',D)

#Vgl mit Litwerten
deltaP = np.abs(100*(Lit2-S2)/Lit2)
deltaD = np.abs(100*(LitD-D)/LitD)
print('relativer Fehler(Position):', deltaP)
print('relativer Fehler(Dicke):',deltaD)
