import matplotlib.pyplot as plt
import numpy as np

#Grundwerte:
e = 1.6022*10**(-19)
c = 299792458
h = 6.6261 * 10**(-34)
dLiF = 201.4 * 10**(-12)

#Winkel:
tCU = 8.8
tKa = 39.6213/2
tKb = 44.2196/2
tGe = 16.2
tBr = 12.7
tBi = 11.1
tZr = 9.4

#Wellenlänge:
lCU = np.sin(tCU*2*np.pi/360)*dLiF*2
lKa = np.sin(tKa*2*np.pi/360)*dLiF*2
lKb = np.sin(tKb*2*np.pi/360)*dLiF*2
lGe = np.sin(tGe*2*np.pi/360)*dLiF*2
lBr = np.sin(tBr*2*np.pi/360)*dLiF*2
lBi = np.sin(tBi*2*np.pi/360)*dLiF*2
lZr = np.sin(tZr*2*np.pi/360)*dLiF*2

#Energie in keV:
ECU = c*h/(lCU*e)
EKa = c*h/(lKa*e)
EKb = c*h/(lKb*e)
EGe = c*h/(lGe*e)
EBr = c*h/(lBr*e)
EBi = c*h/(lBi*e)
EZr = c*h/(lZr*e)

a1 = -np.sqrt(EBr/13.6) + 35

#Ausgabe:
print(
"Wellenlänge, Energie:",
"CU-Röhre:", lCU, ECU,
"CU-Kalpha:", lKa, EKa,
"CU-Kbeta:", lKb, EKb,
"Germanium:", lGe, EGe,
"Brom:", lBr, EBr,
"Bismuth:", lBi, EBi,
"Zirkonium:", lZr, EZr,
"Abschirmzahl:", a1, a2
)
