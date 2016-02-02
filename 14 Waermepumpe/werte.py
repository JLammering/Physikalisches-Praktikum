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
A1 = ufloat(-1e-6, 1e-6)
B1 = ufloat(2.9e-2, 0.2e-2)

A2 = ufloat(5e-6, 2e-6)
B2 = ufloat(-2.9e-2, 0.3e-2)

def diff(t, A, B):
    return 2*A*t + B

print('dT1(240)/dt =', diff(240, A1, B1))
print('dT1(480)/dt =', diff(480, A1, B1))
print('dT1(720)/dt =', diff(720, A1, B1))
print('dT1(960)/dt =', diff(960, A1, B1))

print('')

print('dT2(240)/dt =', diff(240, A2, B2))
print('dT2(480)/dt =', diff(480, A2, B2))
print('dT2(720)/dt =', diff(720, A2, B2))
print('dT2(960)/dt =', diff(960, A2, B2))

A, B, t = sympy.var('A_1 B_1 t')
f = 2*A*t + B
print(f)
print(error(f))
print()
#Aufgabe d(Güteziffer)
cw = ufloat(4.138, 0.01*4.138) #J/(g*K)
rohwasser = 0.998203 #g/cm^3
V1 = ufloat(3000, 1.2) #cm^3
m1 = rohwasser * V1 #g
mkck = ufloat(660, 10)

print('m1 = ',m1)

P = np.genfromtxt('Daten/datenleistung.txt', unpack=True)
Perr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
PmF = unp.uarray(P, Perr)
N = np.mean(PmF)#W

#test
print('N = ', N)

#(m1cw + mkck)dT1/dt *1/N
nu1 = (m1*cw + mkck) * diff(240, A1, B1) *(1/N)
nu2 = (m1*cw + mkck) * diff(480, A1, B1) *(1/N)
nu3 = (m1*cw + mkck) * diff(720, A1, B1) *(1/N)
nu4 = (m1*cw + mkck) * diff(960, A1, B1) *(1/N)
print('')
print('nu1 = ', nu1)
print('nu2 = ', nu2)
print('nu3 = ', nu3)
print('nu4 = ', nu4)

def gueteideal(T1, T2):
    T1 += 273.15
    T2 += 273.15
    return T1/(T1 - T2)

T1oerror = [25.9, 25.9, 40.6, 46.7]
T1error = [0.1, 0.1, 0.1, 0.1]
T1 = unp.uarray(T1oerror, T1error)

T2oerror = [18.4, 11.2, 4.8, 0.0]
T2error = [0.1, 0.1, 0.1, 0.1]
T2 = unp.uarray(T2oerror, T2error)

print('nuid1 = ', gueteideal(T1[0], T2[0]))
print('nuid2 = ', gueteideal(T1[1], T2[1]))
print('nuid3 = ', gueteideal(T1[2], T2[2]))
print('nuid4 = ', gueteideal(T1[3], T2[3]))

def abweich(nure, nuid):
    (nuid-nure)/nuid

print('delta nu1= ', abweich(nu1, gueteideal(T1[0], T2[0])))
print('delta nu2= ', abweich(nu2, gueteideal(T1[1], T2[1])))
print('delta nu3= ', abweich(nu3, gueteideal(T1[2], T2[2])))
print('delta nu4= ', abweich(nu4, gueteideal(T1[3], T2[3])))


m1, cw, mkck, A, t, B, N = sympy.var('m_1 c_w m_kc_k A_1 t B_1 N')
nu = (m1*cw + mkck) * (2*A*t + B) * (1/N)
print(nu)
print(error(nu))
print()

#Aufgabe e(Massendurchsatz)
#(m2cw + mkck)dT2/dt * (1/L)
M = 120.91e-3#kg/mol
L = ufloat(2.09e4, 0.01e4) #J
stoff1 = (m1*cw + mkck) * diff(240, A2, B2) *(1/L)
stoff2 = (m1*cw + mkck) * diff(480, A2, B2) *(1/L)
stoff3 = (m1*cw + mkck) * diff(720, A2, B2) *(1/L)
stoff4 = (m1*cw + mkck) * diff(960, A2, B2) *(1/L)
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

m1, cw, mkck, A, t, B, L, M= sympy.var('m_1 c_w mkck A_2 t B_2 L M')
mass = (m1*cw + mkck) * (2*A*t + B) * (1/L)*M
print(mass)
print(error(mass))
print()

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
nmech2 = nmech(pa[1], pb[1], T2[1], mass1)
nmech3 = nmech(pa[2], pb[2], T2[2], mass1)
nmech4 = nmech(pa[3], pb[3], T2[3], mass1)
print(' ')
print('nmech1 = ',nmech1)
print('nmech2 = ',nmech2)
print('nmech3 = ',nmech3)
print('nmech4 = ',nmech4)

m1, cw, mkck, A, t, B, L, M= sympy.var('m_1 c_w mkck A_2 t B_2 L M')
mass = (m1*cw + mkck) * (2*A*t + B) * (1/L)*M
print(mass)
print(error(mass))
print()
