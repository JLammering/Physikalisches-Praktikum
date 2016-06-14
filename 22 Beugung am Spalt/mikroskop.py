import numpy as np

def abweichung(messung, angabe):
    return abs((angabe-messung)/angabe)

#skala
sq = 0.5/3.2
print('sq= ',sq)

spalt1 = 4/7 *sq
spalt2 = 4/3 * sq
spalt3 = 4*sq
print('spalt1= ',spalt1)
print('Abweichung= ', abweichung(spalt1,0.075))
print('spalt2= ',spalt2)
print('Abweichung= ', abweichung(spalt2,0.15))
print('spalt3= ',spalt3)
print('Abweichung= ', abweichung(spalt3,0.4))

doppellinks = 4*0.23*sq
doppelabstand = 4*(12/13)*sq
print('doppellinks= ',doppellinks)
print('Abweichung= ', abweichung(doppellinks,0.1))
print('doppelabstand= ',doppelabstand)
print('Abweichung= ', abweichung(doppelabstand,0.4))
print('s = ',doppellinks+doppelabstand)
print('Abweichung = ', abweichung(doppellinks+doppelabstand,0.5))
