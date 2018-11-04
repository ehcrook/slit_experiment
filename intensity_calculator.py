#calculate the intensities of the different regular-shaped slit experiments
#these are used as a kind of probability/wave function

import matplotlib.pyplot as plt
import numpy as np
import math

def double_intensity(a, l, D): 
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:   #actual calculation
        stuff = math.pi*a*(1/l)*val*(1/D)
        i = math.sin(stuff)
        i = i**2
        i = i/(stuff**2)
        cos = math.cos(stuff)**2
        i = i*cos
        y.append(i)
    
    #add to output plot
    plt.subplot(121)
    plt.title("Double Slit: Theoretical")
    plt.plot(x,y)
    return [x,y]
    
def single_intensity(a, l, D):
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:   #actual calculation
        stuff = math.pi*a*(1/l)*val*(1/D)
        i = math.sin(stuff)
        i = i**2
        i = i/(stuff**2)
        y.append(i)
        
    #add to output plot
    plt.subplot(121)
    plt.title("Single Slit: Theoretical")
    plt.plot(x,y)
    
    return [x,y]

def n_intensity(n, a, l, D):
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:   #actual calculation
        stuff = 2*math.pi*a*(1/l)*val*(1/D)
        i = 1-math.cos(stuff*n)
        i = i / (1-math.cos(stuff))
        y.append(i)
        
    #add to output plot
    plt.subplot(121)
    plt.title("N-Slit: Theoretical")
    plt.plot(x,y)

    return [x,y]