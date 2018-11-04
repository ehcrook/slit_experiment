import poppy



def circular_intensity(wvl, pupil_radius, pixel_scale_par = 0.009):
    """ Calculate and plot circular intensity
        circular_intensity(wvl, pupil_radius, pixel_scale_par = 0.05)
        wvl : wavelength in microns
    """
        
    osys = poppy.OpticalSystem()
    osys.add_pupil( poppy.CircularAperture(radius = pupil_radius))    # pupil radius in meters
    planeCor = pupil_radius  # This line will let us change coordinates of the plane according to the pupil radius to better represent the diffraction pattern
    if pupil_radius <= 0.49:
        planeCor = pupil_radius * 10
    osys.add_detector(pixelscale=pixel_scale_par, fov_arcsec=planeCor)  # image plane coordinates in arcseconds

    psf = osys.calc_psf(wvl)                            # wavelength in meters
    poppy.display_psf(psf, title='The Circular Aperture')
