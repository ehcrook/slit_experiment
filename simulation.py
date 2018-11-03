from __future__ import division
from numpy import *
import scipy
from scipy.special import fresnel

def diffract(independent):
    h = 6.62606896e-34
    electronMass= 9.10938188e-31 # Kg
    c = 299792458    
    momentum = 0.01*c*electronMass
    wavelen = h / momentum
    x = independent
    a = 0.1e-8
    b = 1e-6
    d1 = 1
    d2 = 1
    inot = 1
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
    return diffract


if __name__ == "__main__":
    import sys
    from pylab import *
   
    # Convert all command line arguments to floats.
    inputs = sys.argv[1:]
    parameters = [float(input) for input in inputs]
   
    # Generate the plot.
    x = arange(-pi, pi, 0.01)
    y = list()
    for val in x:
        y.append(diffract(val))
   
    # Display it using the builtin graphical interface.
    plot(x, y)
    show()    