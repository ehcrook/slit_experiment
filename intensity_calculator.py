#calculate the intensities of the different slit experiments
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
    plt.plot(x,y)

    return [x,y]

def circular_intensity_plot(waveLen, pixel_size = 0.05, pixelsXY = 80):
    import inspect
    import numpy
    import matplotlib.pyplot as pyplot
    import microscPSF.microscPSF as msPSF
    mp = msPSF.m_params
    rv = np.arange(0.0, 6.01, pixel_size)
    zv = np.arange(-3.01, 3.01, pixel_size)
    waveLen *= 1.E-3
    
    def psfSlicePics(psf, sxy, sz, pixel_size):
        
        ex = pixel_size * 0.5 * psf.shape[1]
        ez = pixel_size * (0.5 * psf.shape[0])

        fig = pyplot.figure(figsize = (12,4))
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

    pyplot.show()
    
    psf_xyz = msPSF.gLXYZFocalScan(mp, pixel_size, pixelsXY, zv, normalize = False, wvl = waveLen)
    psfSlicePics(psf_xyz, 15, 30, pixel_size)
