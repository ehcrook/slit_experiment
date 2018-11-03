#calculate the intensities of single and double slit experiments

import matplotlib.pyplot as plt
import numpy as np
import pandas as p
import math

def double_intensity(n): 
    x = np.linspace(-10,10,10000)
    y = (1/(x**2)) * (np.cos(n*x)**2) * (np.sin(x)**2)
    plt.plot(x,y)
    plt.show()
    return 
    
def single_intensity(n, a, l, D):
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:
        stuff = math.pi*a*(1/l)*val*(1/D)
        i = math.sin(stuff)
        i = i**2
        i = i/(stuff**2)
        y.append(i)
    plt.plot(x,y)
    plt.show()
    return [x,y]