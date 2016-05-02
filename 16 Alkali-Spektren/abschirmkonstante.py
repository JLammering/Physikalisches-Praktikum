import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

eichgroesse = ufloat(2.131e-11, 0.003e-11)#m/Skt
g = ufloat(1.022e-6, 0.003e-6)#m
h = ufloat(6.626070040e-34, 0.000000081e-34)#Js
c = 299792458#m/s
e = ufloat(1.6021766208e-19, 0.0000000098e-19)#C
Rinfty = ufloat(13.605693009, 0.000000084)#eV
alpha = ufloat(7.2973525664e-3, 0.0000000017e-3)

def sigma2(delEd, n, z):
    return z-(delEd*2*(n**3/(Rinfty*alpha**2)))**(1/4)

#natrium
#rot, gelb, gruengelb

phi_na = np.array([267.7, 269.6, 271.0])
phi_na = 305.3 - phi_na
phi_na *= (1/360)*2*np.pi
dels_na = np.array([27, 30, 24])
lamda_na = unp.sin(phi_na)*g
dellamda_na = eichgroesse * unp.cos(phi_na) * dels_na
delEd_na = h*c*(dellamda_na/lamda_na**2)
delEd_na /= e #in eV umrechnen
sigma_na = sigma2(delEd_na, 3, 11)

print('natrium: ')
print('phi_na: ', phi_na)
print('lamda_na:', lamda_na)
print('dellamda_na: ', dellamda_na)
print('delEd_na: ', delEd_na)
print('sigma_na: ', sigma_na)

#Kalium
#Reihenfloge gelb1, gelb2, grün1, grün2
def mittelwert(phi_1, phi_2):
    a = np.array([phi_1, phi_2])
    x = np.mean(a)
    y = np.std(a)
    return ufloat(x, y)

phi_kagelb1 = np.array([270.5, 270.4])
phi_kagelb2 = np.array([270.3, 270.4])
phi_kagruen1 =np.array([273.7, 273.6])
phi_kagruen2 =np.array([273.5, 273.4])
phi_ka = unp.uarray([np.mean(phi_kagelb1), np.mean(phi_kagelb2), np.mean(phi_kagruen1), np.mean(phi_kagruen2)],
[np.std(phi_kagelb1), np.std(phi_kagelb2), np.std(phi_kagruen1), np.std(phi_kagruen2)])
phi_ka = 305.3 - phi_ka
phi_ka *= (1/360)*2*np.pi
dels_ka = np.array([85, 15, 81, 67])
lamda_ka = unp.sin(phi_ka)*g
dellamda_ka = eichgroesse * unp.cos(phi_ka) * dels_ka
delEd_ka = h*c*(dellamda_ka/lamda_ka**2)
delEd_ka /= e #in eV umrechnen
sigma_ka = sigma2(delEd_ka, 4, 19)

print('Kalium: ')
print('phi_ka: ', phi_ka)
print('lamda_ka:', lamda_ka)
print('dellamda_ka: ', dellamda_ka)
print('delEd_ka: ', delEd_ka)
print('sigma_ka: ', sigma_ka)


#Rubidium
#ein rotes Dublett

phi_ru1 = np.array([267.4, 266.7])
phi_ru = unp.uarray([np.mean(phi_ru1)], [np.std(phi_ru1)])
phi_ru = 305.3 - phi_ru
phi_ru *= (1/360)*2*np.pi
dels_ru = np.array([27])
lamda_ru = unp.sin(phi_ru)*g
dellamda_ru = eichgroesse * unp.cos(phi_ru) * dels_ru
delEd_ru = h*c*(dellamda_ru/lamda_ru**2)
delEd_ru /= e #in eV umrechnen
sigma_ru = sigma2(delEd_ru, 5, 37)

print('Rubidium: ')
print('phi_ru: ', phi_ru)
print('lamda_ru:', lamda_ru)
print('dellamda_ru: ', dellamda_ru)
print('delEd_ru: ', delEd_ru)
print('sigma_ru: ', sigma_ru)
