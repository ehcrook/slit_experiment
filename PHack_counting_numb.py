import matplotlib.pyplot as plt
import numpy as np
import pandas as p
from math import *



n = int(input("Enter counting number: "))
#N = np.array(range(10)) #counting number


x = np.linspace(-10,10,100)
y = (1/(x**2)) * (np.cos(n*x)**2) * (np.sin(x)**2)
plt.plot(x,y)
plt.show()

