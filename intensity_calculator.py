#calculate the intensities of the different slit experiments
#these are used as a kind of probability/wave function

import matplotlib.pyplot as plt
import numpy as np
import pandas as p
import math

def double_intensity(n, a, l, D): 
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:
        stuff = math.pi*a*(1/l)*val*(1/D)
        i = math.sin(stuff)
        i = i**2
        i = i/(stuff**2)
        cos = math.cos(stuff)**2
        i = i*cos
        y.append(i)    
    plt.subplot(121)
    plt.plot(x,y)
    return [x,y]
    
def single_intensity(n, a, l, D):
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:
        stuff = math.pi*a*(1/l)*val*(1/D)
        i = math.sin(stuff)
        i = i**2
        i = i/(stuff**2)
        y.append(i)
    plt.subplot(121)
    plt.plot(x,y)
    
    return [x,y]