import numpy as np
import matplotlib.pyplot as plt
import math as math

l = input("enter a wavelength (nm): ")
l = float(l) * (10**-9)
a = input("enter a slit width (micro m): ")
a = float(a) * (10**-6) 
D = input("enter a distance from the screen (m): ")
D = float(D)

I0 = 100
I = list()
I2 = list()

endpoint = (D*l)/a
y = np.linspace(-5*endpoint,5*endpoint,10000)

#single slit
for val in y:
    stuff = math.pi*a*(1/l)*val*(1/D)
    i = math.sin(stuff)
    i = i**2
    i = i/(stuff**2)
    #i = i * I0
    I.append(i)
    """
    stuff2 = math.pi*a*(1/l)*np.arctan(val/D)
    i2 = math.cos(stuff2)
    i2 = i2**2
    I2.append(i2)
    """

plot = plt.plot(y, I)
plt.show()
