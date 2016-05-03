import numpy as np

def alpha(theta, cl, cp):
    c = cl/cp
    return(90- np.arcsin(theta * c))

cl= 1150
cp= 2700
