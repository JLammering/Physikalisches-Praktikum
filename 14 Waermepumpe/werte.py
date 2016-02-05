import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import sympy

#Fehler:
def error(f, err_vars=None):
    from sympy import Symbol, latex
    s=0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

E, q, r = sympy.var('E_x q r')
f = E + q**2 * r
print(f)
print(error(f))
print()

#Aufgabe c(Differentialquotienten)
A1 = ufloat(-2e-8, 0.1e-8)
B1 = ufloat(2.6e-5, 0.3e-5)
C1 = ufloat(2e-2, 0.2e-2)

A2 = ufloat(3e-8, 0.2e-8)
B2 = ufloat(-4.6e-5, 0.4e-5)
C2 = ufloat(-6.4e-3, 2e-3)

def diff(t, A, B, C):
    return 3*A*t**2 + 2*B*t + C

dT1_240 = diff(240, A1, B1, C1)
dT1_480 = diff(480, A1, B1, C1)
dT1_720 = diff(720, A1, B1, C1)
dT1_960 = diff(960, A1, B1, C1)
print('dT1(240)/dt =', dT1_240)
print('dT1(480)/dt =', dT1_480)
print('dT1(720)/dt =', dT1_720)
print('dT1(960)/dt =', dT1_960)

print('')

dT2_240 = diff(240, A2, B2, C2)
dT2_480 = diff(480, A2, B2, C2)
dT2_720 = diff(720, A2, B2, C2)
dT2_960 = diff(960, A2, B2, C2)
print('dT2(240)/dt =', dT2_240)
print('dT2(480)/dt =', dT2_480)
print('dT2(720)/dt =', dT2_720)
print('dT2(960)/dt =', dT2_960)

A, B, t = sympy.var('A_1 B_1 t')
f = 2*A*t + B
#print(f)
#print(error(f))
#print()
#Aufgabe d(Güteziffer)
cw = ufloat(4.138, 0.01*4.138) #J/(g*K)
rohwasser = 0.998203 #g/cm^3
V1 = ufloat(3000, 1.2) #cm^3
m1 = rohwasser * V1 #g
mkck = ufloat(660, 10)

print('m1 = ',m1)

P, t = np.genfromtxt('Daten/datenleistung.txt', unpack=True)
Perr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
PmF = unp.uarray(P, Perr)
#N = np.mean(PmF)#W

#test
#print('N = ', N)

#(m1cw + mkck)dT1/dt *1/N
nu1 = (m1*cw + mkck) * dT1_240 *(1/PmF[4])
nu2 = (m1*cw + mkck) * dT1_480 *(1/PmF[8])
nu3 = (m1*cw + mkck) * dT1_720 *(1/PmF[12])
nu4 = (m1*cw + mkck) * dT1_960 *(1/PmF[16])
print('')
print('nu1 = ', nu1)
print('nu2 = ', nu2)
print('nu3 = ', nu3)
print('nu4 = ', nu4)

def gueteideal(T1, T2):
    T1 += 273.15
    T2 += 273.15
    return T1/(T1 - T2)

T1oerror = [25.9, 33.5, 40.6, 46.7]
T1error = [0.1, 0.1, 0.1, 0.1]
T1 = unp.uarray(T1oerror, T1error)

T2oerror = [18.4, 11.2, 4.8, 0.0]
T2error = [0.1, 0.1, 0.1, 0.1]
T2 = unp.uarray(T2oerror, T2error)

#lol = (T1+273.15)/((T1+273.15) - (T2+273.15))
#print('lol1 = ', lol[0])

nuid1 = gueteideal(T1[0], T2[0])
nuid2 = gueteideal(T1[1], T2[1])
nuid3 = gueteideal(T1[2], T2[2])
nuid4 = gueteideal(T1[3], T2[3])
print('nuid1 = ', nuid1)
print('nuid2 = ', nuid2)
print('nuid3 = ', nuid3)
print('nuid4 = ', nuid4)
print()

def abweich(nure, nuid):
    return (nuid-nure)/nuid

print('delta nu1= ', abweich(nu1, nuid1))
print('delta nu2= ', abweich(nu2, nuid2))
print('delta nu3= ', abweich(nu3, nuid3))
print('delta nu4= ', abweich(nu4, nuid4))


#m1, cw, mkck, A, t, B, N = sympy.var('m_1 c_w m_kc_k A_1 t B_1 N')
#nu = (m1*cw + mkck) * (2*A*t + B) * (1/N)
#print(nu)
#print(error(nu))
#print()

#Aufgabe e(Massendurchsatz)
#(m2cw + mkck)dT2/dt * (1/L)
M = 120.91e-3#kg/mol
L = ufloat(2.09e4, 0.01e4) #J/mol
stoff1 = (m1*cw + mkck) * dT2_240 / L
stoff2 = (m1*cw + mkck) * dT2_480 * (1/L)
stoff3 = (m1*cw + mkck) * dT2_720 * (1/L)
stoff4 = (m1*cw + mkck) * dT2_960 * (1/L)
mass1 = stoff1 * M
mass2 = stoff2 * M
mass3 = stoff3 * M
mass4 = stoff4 * M
print('')
print('stoff1 = ', stoff1, 'mol/s')
print('stoff2 = ', stoff2, 'mol/s')
print('stoff3 = ', stoff3, 'mol/s')
print('stoff4 = ', stoff4, 'mol/s')

print('')
print('mass1 = ', mass1*10**3, 'g/s')
print('mass2 = ', mass2*10**3, 'g/s')
print('mass3 = ', mass3*10**3, 'g/s')
print('mass4 = ', mass4*10**3, 'g/s')

#m1, cw, mkck, A, t, B, L, M= sympy.var('m_1 c_w mkck A_2 t B_2 L M')
#mass = (m1*cw + mkck) * (2*A*t + B) * (1/L)*M
#print(mass)
#print(error(mass))
#print()

#Aufgabe f(mech. Leistung)
kappa = 1.14
roh0 = 5.51 #g/l
p0 = 1#bar
T0 = 273.15#kelvin

paoerror = [3.1, 3.1, 3.2, 3.2]
paerror = [0.2, 0.2, 0.2, 0.2]
pa = unp.uarray(paoerror, paerror)

pboerror = [8.1, 9.8, 11.4, 12.9]
pberror = [0.2, 0.2, 0.2, 0.2]
pb = unp.uarray(pboerror, pberror)

T2oerror = [18.4+273.15, 11.2+273.15, 4.8+273.15, 0.0+273.15]
T2error = [0.1, 0.1, 0.1, 0.1]
T2 = unp.uarray(T2oerror, T2error)

def nmech(pa, pb, T2, mass):
    return (1/(kappa - 1))* (pb*(pa/pb)**(1/kappa) - pa)*(T2*p0/(roh0*T0*pa))*mass*10**5

nmech1 = nmech(pa[0], pb[0], T2[0], mass1)
nmech2 = nmech(pa[1], pb[1], T2[1], mass2)
nmech3 = nmech(pa[2], pb[2], T2[2], mass3)
nmech4 = nmech(pa[3], pb[3], T2[3], mass4)
print(' ')
print('nmech1 = ',nmech1)
print('nmech2 = ',nmech2)
print('nmech3 = ',nmech3)
print('nmech4 = ',nmech4)

roh = (roh0*T0*pa)/(T2*1)

print()
print('roh1 = ', roh[0])
print('roh2 = ', roh[1])
print('roh3 = ', roh[2])
print('roh4 = ', roh[3])


m1, cw, mkck, A, t, B, L, M= sympy.var('m_1 c_w mkck A_2 t B_2 L M')
mass = (m1*cw + mkck) * (2*A*t + B) * (1/L)*M
#print(mass)
#print(error(mass))
#print()
