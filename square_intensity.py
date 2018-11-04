import matplotlib.pyplot as plt
import numpy as np
import math

#x: xscreen: starting position on screen(m)
#y: yscreen: starting postition on screen(m)

def square_intensity(a, l, D):
    x = np.linspace(-10, 10, 10000) ##??
    y = np.linspace(-10, 10, 10000) ##??
    y = list()
    for val in x:
        stuff_x = ((2*np.pi*a*val) / (l*D))
        stuff_y = ((2*np.pi*a*val) / (l*D))
        j = ((math.sin(stuff_x)) / (stuff_x))**2
        k = ((math.sin(stuff_y)) / (stuff_y))**2
        i = j * k
        y.append(i)

    plt.plot(x, y)
    plt.title("Square: Theoretical")
    plt.show()
    return[x, y]



#test

def input_():
    #user inputs
    l = input("enter a wavelength (nm): ")
    l = float(l) * (10**-9)
    a = input("enter a slit width (micro m): ")      #for single slit
    a = float(a) * (10**-6)
    #d = input("enter a slit separation (micro m): ") #for double slit
    #d = float(d) * (10**-10)
    D = input("enter a distance from the screen (m): ")
    D = float(D)
    #N = input("enter number of slits: ")             #for n slit
    #N = int(N)
    #num = input("finally, input the number of particles: ")
    #num = int(num)

    square_intensity(a, N, D, l)


if __name__ == "__main__":
    #run
    input_()