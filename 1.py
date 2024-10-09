import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def s(x):
    return -1.6*x**2+1.3*x+141.3 

def r(x):
    return 1.4*x**2-5.6*x+12.6

def inter(x):
    return s(x)-r(x)

xo = np.linspace(-50, 50, 2)
solucion = fsolve(inter, xo)

print(solucion)

print("----------------------------------------------------------------------------------")

