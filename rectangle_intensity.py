# Calculate light intensity based when it goes through a specified rectangular slit
import poppy 

def rectangle_intensity(rot = 0, wd= 2,ht = 1, xshi = 0,yshi = 0):
    """Calculate light intensity for light going through a rectangular slit
    rectangle_intensity(rot = 0, wd= 2,ht = 1, xshi = 0,yshi = 0)
    
    rot : rotation in degrees
    
    wd : width in m
    
    ht : height in m
    
    xshi : x axis shift in m
    
    yshi : y axis shift in m
    
    """
    ap = poppy.RectangleAperture(rotation= rot,width=wd,height= ht, shift_x=xshi,shift_y = yshi)
    ap.display(colorbar=False)
    
    osys = poppy.OpticalSystem()
    osys.add_pupil(ap)
    osys.add_detector(pixelscale=0.05, fov_arcsec=2.0)
    psf = osys.calc_psf(1e-6)

    plt.figure(figsize=(12,8))
    poppy.display_psf(psf, title="Diffraction Pattern")
    
    
    
