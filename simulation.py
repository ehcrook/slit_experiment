from __future__ import division
import numpy as np
import scipy
from scipy.special import fresnel
import matplotlib.pyplot as plt

def diffract(num, m, a, b):
    h = 6.62606896e-34
    electronMass= 9.10938188e-31
    c = 299792458    
    momentum = 0.01*c*electronMass
    wavelen = h / m
    x = np.linspace(-10,10,10000)
    d1 = 1
    d2 = 1
    inot = 1
    intensity = list()
    
    for val in x:
        y = ((2 / wavelen) * ((1/d1) + (1/d2)))**(1/2)
        
        utop1 = y * ((d1/(d1+d2)) * (x + (b/2)) + (a/2))
        utop2 = y * ((d1/(d1+d2)) * (x + (b/2)) - (a/2))
        
        ubottom1 = y * ((d1/(d1+d2)) * (x - (b/2)) + (a/2))
        ubottom2 = y * ((d1/(d1+d2)) * (x - (b/2)) - (a/2))
                
        (ssat2, ccat2) = scipy.special.fresnel(utop2)
        (ssat1, ccat1) = scipy.special.fresnel(utop1)
        
        (ssab2, ccab2) = scipy.special.fresnel(ubottom2)
        (ssab1, ccab1) = scipy.special.fresnel(ubottom1)
        
        fsin1 = ssat1 - ssat2
        fcos1 = ccat1 - ccat2
        fint1 = fcos1 + (fsin1*1j)
        
        fsin2 = ssab1 - ssab2
        fcos2 = ccab1 - ccab2
        fint2 = fcos2 + (fsin2*1j)
                
        finttotal = abs(fint1 + fint2)
        diffract = 1/2 * 1 * (finttotal**2)
        intensity.append(diffract)
    
    plt.subplot(121)
    plt.plot(x,intensity)    
    
    return [x, intensity]