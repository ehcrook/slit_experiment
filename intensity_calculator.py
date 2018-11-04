#calculate the intensities of the different slit experiments
#these are used as a kind of probability/wave function

import matplotlib.pyplot as plt
import numpy as np
import math
import microscPSF as msPSF
import inspect

def double_intensity(a, l, D): 
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
    
def single_intensity(a, l, D):
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

def n_intensity(n, a, l, D):
    x = np.linspace(-10,10,10000)
    y = list()
    for val in x:
        stuff = 2*math.pi*a*(1/l)*val*(1/D)
        i = 1-math.cos(stuff*n)
        i = i / (1-math.cos(stuff))
        y.append(i)
    plt.subplot(121)
    plt.plot(x,y)

    return [x,y]

#equation for use with circular apertures
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

def circular_intensity_plot(waveLen, pixel_size, pixelsXY):
    mp = msPSF.m_params
    rv = np.arange(0.0, 6.01, pixel_size)
    zv = np.arange(-3.01, 3.01, pixel_size)
    
    psf_xyz = msPSF.gLXYZFocalScan(mp, zv, pixel_size, pixelsXY, normalize = False, wvl = waveLen)
    psfSlicePics(psf_xyz, 15, 30, pixel_size)
    
    plt.show()
    
#intensity calculation for a triangular aperture
def triangle(a, l, D):
    #3 dimensional intensity distribution
    #point of triangles at (0,0), (a, a), (a,-a)
    
    x = np.linspace(0,a,10000)

    xy = list()     #list of (x,y) coords that resulted in the z val
    z = list()
    
    for kx in x:
        for ky in range(-kx, kx, 20*kx):    #pick x values in shape of triangle
            xy.append( (kx,ky) )
            k = 2*math.pi/l
            one = (2*a*math.exp(1j*k*D))/(1j*ky*z)
            two = math.exp(-1j*(kx-ky)*a/2)
            four = math.exp(-1j*(kx+ky)*a/2)
            three = np.sinc((kx-ky)*a/(2*math.pi))
            five = np.sinc((kx+ky)*a/(2*math.pi))        
            z.append(one*(two*three-four*five))
            
    return [xy, z]

if __name__ == "__main__":
    circular_intensity_plot(900e-9,0.05,80)