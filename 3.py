import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def m(x):
    return x**3-4*x**2+5*x

print (f"{m(10)}")

