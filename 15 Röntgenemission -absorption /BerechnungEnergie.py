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
tBi1 = 10.7
tBi2 = 12.8
tZr = 9.4

#Wellenlänge:
lCU = np.sin(tCU*2*np.pi/360)*dLiF*2
lKa = np.sin(tKa*2*np.pi/360)*dLiF*2
lKb = np.sin(tKb*2*np.pi/360)*dLiF*2
lGe = np.sin(tGe*2*np.pi/360)*dLiF*2
lBr = np.sin(tBr*2*np.pi/360)*dLiF*2
lBi1 = np.sin(tBi1*2*np.pi/360)*dLiF*2
lBi2 = np.sin(tBi2*2*np.pi/360)*dLiF*2
lZr = np.sin(tZr*2*np.pi/360)*dLiF*2

#Energie in keV:
ECU = c*h/(lCU*e)
EKa = c*h/(lKa*e)
EKb = c*h/(lKb*e)
EGe = c*h/(lGe*e)
EBr = c*h/(lBr*e)
EBi1 = c*h/(lBi1*e)
EBi2 = c*h/(lBi2*e)
EZr = c*h/(lZr*e)

#Ausgabe:
print(
"Wellenlänge, Energie:",
"CU-Röhre:", lCU, ECU,
"CU-Kalpha:", lKa, EKa,
"CU-Kbeta:", lKb, EKb,
"Germanium:", lGe, EGe,
"Brom:", lBr, EBr,
"Bismuth1:", lBi1, EBi1,
"Bismuth2:", lBi2, EBi2,
"Zirkonium:", lZr, EZr,
"Energiedifferenz Kupfer:", EKa-EKb
)
