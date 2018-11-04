import inspect
import numpy as np
import matplotlib.pyplot as plt
import microscPSF as msPSF
from mpl_toolkits.mplot3d import Axes3D

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

def circular_intensity(waveLen, pixel_size = 0.05, pixelsXY = 80):
    mp = msPSF.m_params
    rv = np.arange(0.0, 6.01, pixel_size)
    zv = np.arange(-3.01, 3.01, pixel_size)
    #waveLen *= 1.E-3
    
    psf_xyz = msPSF.gLXYZFocalScan(mp, zv, pixel_size, pixelsXY, normalize = False, wvl = waveLen)
    psfSlicePics(psf_xyz, 15, 30, pixel_size)
    
    plt.show()
