#calculate the intensities of the different slit experiments
#these are used as a kind of probability/wave function

import matplotlib.pyplot as plt
import numpy as np
import math
import microscPSF as msPSF
import inspect
from mpl_toolkits.mplot3d import Axes3D

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
    plt.title("Theoretical")
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
    plt.title("Theoretical")
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
    plt.title("Theoretical")
    plt.plot(x,y)

    return [x,y]

"""
# UNEDITED CIRCULAR APERTURE
def circular_intensity_plot(waveLen, pixel_size = 0.05, pixelsXY = 80):
    import inspect
    import numpy
    import matplotlib.plt as plt
    import microscPSF.microscPSF as msPSF
    mp = msPSF.m_params
    rv = np.arange(0.0, 6.01, pixel_size)
    zv = np.arange(-3.01, 3.01, pixel_size)
    waveLen *= 1.E-3
    
    def psfSlicePics(psf, sxy, sz, pixel_size):
        
        ex = pixel_size * 0.5 * psf.shape[1]
        ez = pixel_size * (0.5 * psf.shape[0])

        fig = plt.figure(figsize = (12,4))
        ax1 = fig.add_subplot(1,3,1)
        ax1.imshow(numpy.sqrt(psf[sz,:,:]),
               interpolation = 'none', 
               extent = [-ex, ex, -ex, ex],
               cmap = "gray")
        ax1.set_title("PSF XY slice")

        ax2 = fig.add_subplot(1,3,2)
        ax2.imshow(numpy.sqrt(psf[:,:,sxy]),
               interpolation = 'none',
               extent = [-ex, ex, -ez, ez],
               cmap = "gray")
        ax2.set_title("PSF YZ slice")
    
        ax3 = fig.add_subplot(1,3,3)
        ax3.imshow(numpy.sqrt(psf[:,sxy,:]), 
               interpolation = 'none',
               extent = [-ex, ex, -ez, ez],
               cmap = "gray")
        ax3.set_title("PSF XZ slice")

    plt.show()
    
    psf_xyz = msPSF.gLXYZFocalScan(mp, pixel_size, pixelsXY, zv, normalize = False, wvl = waveLen)
    psfSlicePics(psf_xyz, 15, 30, pixel_size)
"""

def psfSlicePics(psf, sxy, sz, pixel_size):
    ex = pixel_size * 0.5 * psf.shape[1]
    ez = pixel_size * (0.5 * psf.shape[0])

    fig = plt.figure(figsize = (12,4))
    ax1 = fig.add_subplot(1,3,1)
    ax1.imshow(np.sqrt(psf[sz,:,:]),
           interpolation = 'none', 
           extent = [-ex, ex, -ex, ex],
           cmap = "gray")
    ax1.set_title("PSF XY slice")

    ax2 = fig.add_subplot(1,3,2)
    ax2.imshow(np.sqrt(psf[:,:,sxy]),
           interpolation = 'none',
           extent = [-ex, ex, -ez, ez],
           cmap = "gray")
    ax2.set_title("PSF YZ slice")

    ax3 = fig.add_subplot(1,3,3)
    ax3.imshow(np.sqrt(psf[:,sxy,:]), 
           interpolation = 'none',
           extent = [-ex, ex, -ez, ez],
           cmap = "gray")
    ax3.set_title("PSF XZ slice")

def circular_intensity_plot(waveLen, pixel_size = 0.05, pixelsXY = 80):
    mp = msPSF.m_params
    rv = np.arange(0.0, 6.01, pixel_size)
    zv = np.arange(-3.01, 3.01, pixel_size)
    #waveLen *= 1.E-3
    
    psf_xyz = msPSF.gLXYZFocalScan(mp, zv, pixel_size, pixelsXY, normalize = False, wvl = waveLen)
    psfSlicePics(psf_xyz, 15, 30, pixel_size)
    
    plt.show()
    
def triangle(a, l, D):
    #3 dimensional intensity distribution
    #point of triangles at (0,0), (a, a), (a,-a)
    
    x = np.linspace(0,1,10000)
    X = list()       #list of X coords that resulted in the z val
    Y = list()       #list of Y coords that resulted in the z val
    z = list()
    
    for kx in x:
        Y_ = np.linspace(-kx, kx, 20*kx)
        for ky in Y_:    #pick x values in shape of triangle
            X.append(kx)
            Y.append(ky)
            k = 2*math.pi/l
            """
            one = (2*a*math.exp(1j*k*D))/(1j*ky*D)
            two = math.exp(-1j*(kx-ky)*a/2)
            four = math.exp(-1j*(kx+ky)*a/2)
            three = np.sinc((kx-ky)*a/(2*math.pi))
            five = np.sinc((kx+ky)*a/(2*math.pi))   
            """
            one = (2*a*math.exp(k*D))/(ky*D)
            two = math.exp(-1*(kx-ky)*a/2)
            four = math.exp(-1*(kx+ky)*a/2)
            three = np.sinc((kx-ky)*a/(2*math.pi))
            five = np.sinc((kx+ky)*a/(2*math.pi))        
            z.append(one*(two*three-four*five))
            
    print(X)
    print(Y)
    print(z)
    
    # A 3D PLOT WOULD BE NICE
    plt.subplot(121, projection='3d')
    plt.title("Theoretical")
    plt.scatter(X, Y, z, c='r', marker='o')  
            
    return [(X,Y), z]

if __name__ == "__main__":
    triangle(5e-6,900e-9,1)
    plt.show()