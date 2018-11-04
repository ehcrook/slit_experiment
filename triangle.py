def triangle_intensity(a, l, D):
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
    plt.title("Triangle: Theoretical")
    plt.scatter(X, Y, z, c='r', marker='o')  
            
    return [(X,Y), z]

if __name__ == "__main__":
    triangle(5e-6,900e-9,1)
    plt.show()