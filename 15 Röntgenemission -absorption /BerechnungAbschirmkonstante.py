import matplotlib.pyplot as plt
import numpy as np

R = 13.6
alpha =  7.297* 10**-3

ZCU = 29
ECU = 904.1

Zge = 32
Ege = 11032.8

Zbr = 35
Ebr = 14000.8

Zzr = 40
Ezr = 18845.9

Zbi = 83
Ebi = 16578.2 - 13893.2

EGelit = 11103.6
EBrlit = 13474.1
EZrlit = 17996.2
#EBilit = 16390.0

#Eu = Zge**2*R

sigmaCU = ZCU - np.sqrt((ECU)/R - alpha**2/4 * ZCU**4)

sigmaGe = Zge - np.sqrt((Ege)/R - alpha**2/4 * Zge**4)
sigmaGelit = Zge - np.sqrt((EGelit)/R - alpha**2/4 * Zge**4)

sigmaBr = Zbr - np.sqrt((Ebr)/R - alpha**2/4 * Zbr**4)
sigmaBrlit = Zbr - np.sqrt((EBrlit)/R - alpha**2/4 * Zbr**4)

sigmaZr = Zzr - np.sqrt((Ezr)/R - alpha**2/4 * Zzr**4)
sigmaZrlit = Zzr - np.sqrt((EZrlit)/R - alpha**2/4 * Zzr**4)

sigmaBi = Zbi - np.sqrt((4/alpha * np.sqrt(Ebi/R) - 5*Ebi/R))*np.sqrt(1+ 19/32 * alpha**2 *Ebi/R)
#sigmaBilit = Zbi - np.sqrt((4/alpha * np.sqrt(EBilit/R) - 5*EBilit/R)*np.sqrt(1+ 19/32 * alpha**2 *EBilit/R))

print(
"Abschirmkonstanten(mess, lit):",
"Kupfer:",sigmaCU,
"Germanium:",sigmaGe,sigmaGelit,
"Brom:",sigmaBr,sigmaBrlit,
"Zirkonium:",sigmaZr,sigmaZrlit,
"Bismuth:",sigmaBi
)
