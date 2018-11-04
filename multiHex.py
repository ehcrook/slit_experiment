import poppy

%pylab inline --no-import-all
    

def display_multiHex(rings_number_mother, sec_rad_mother, side_dist_mother = 1.0,segment_gap_mother = 0.01, pixel_scale = 0.010, fov_arcsec_mag = 2.0, figure_size = (12 ,8),wvl = 1e-6):
    
    def multi_hexagon(rings_number, sec_rad, side_dist = 1.0, segment_gap = 0.01):
            """ 
    multi_hexagon(rings_number, sec_rad, side_dist = 1.0, segment_gap = 0.01)
    # rings : The number of rings of hexagons to include, not counting the central segment
    
    # side_dist : Distance between sides (flat-to-flat) of the hexagon, in meters. Default is 1.0
    
    # segment_gap : Gap between adjacent segments, in meters. Default is 0.01 m = 1 cm
    
    # sec_rad : scondary obstacle radius
        
            """
        
            ap = poppy.MultiHexagonAperture(name='ApertureHex', flattoflat = side_dist, gap = segment_gap,rings =rings_number)  # 3 rings of 2 m segments yields 14.1 m circumscribed diameter
            sec = poppy.SecondaryObscuration(secondary_radius = float(sec_rad), n_supports = 4, support_width = 0.1)   # secondary with spiders
            atlast = poppy.CompoundAnalyticOptic( opticslist=[ap, sec], name='Mock ATLAST')           # combine into one optic
        
            plt.figure(figsize=(12,8))
            atlast.display(npix=1024, colorbar_orientation='vertical')
            return atlast
    
    osys = poppy.OpticalSystem()
    osys.add_pupil(multi_hexagon(rings_number_mother,sec_rad_mother,side_dist_mother,segment_gap_mother))
    osys.add_detector(pixelscale=pixel_scale, fov_arcsec=fov_arcsec_mag)
    psf = osys.calc_psf(wvl)

    plt.figure(figsize=figure_size)
    poppy.display_psf(psf, title="Diffraction Pattern")
    
