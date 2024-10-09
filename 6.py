import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def s(n):
    return 2*n**2+3*n+5

print(f"{s(50)}")