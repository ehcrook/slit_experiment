#code for the step functionality
#showing the particles being added one by one
#basically a simulation of the slit experiment

import intensity_calculator as ic
import square_intensity as sq
import matplotlib.pyplot as plt
import numpy as np
import buckets as B

def make_dict(x):
    points = dict()
    for i in x:
        if i in points:
            points[i] += 1
        else:
            points[i] = 1
    return points
        
def step():
    a = 6e-9
    l = 900e-9
    D = 1
    n = 10
    
    values1 = ic.single_intensity(a,l,D)
    intensity1 = values1[1]
    x_vals1 = values1[0]  
    values2 = ic.double_intensity(a, l, D)
    intensity2 = values2[1]
    x_vals2 = values2[0]      
    valuesN = ic.n_intensity(n,a,l,D)
    intensityN = valuesN[1]
    x_valsN = valuesN[0]      
    valuesSq = sq.square_intensity(a,l,D)
    intensitySq = valuesSq[1]
    x_valsSq = valuesSq[0] 
    
    x1 = list()
    x2 = list()
    xN = list()
    xSq = list()    
    
    plt.figure(figsize = (20,10), tight_layout = True)
    
    step = True
    while(step == True):
        num = input("How many particles? ('stop' to stop): ")
        if(num == "stop"):
            step = False
            continue
    
        num = int(num)
    
        i = 0
        while i < num:
            x1.append(B.call_bucket(values1,intensity1))
            x2.append(B.call_bucket(values2,intensity2))
            xN.append(B.call_bucket(valuesN,intensityN))
            xSq.append(B.call_bucket(valuesSq,intensitySq))
            
    points1 = make_dict(x1)
    points2 = make_dict(x2)
    pointsN = make_dict(xN)
    pointsSq = make_dict(xSq)
        
    plt.subplot(221)
    plt.scatter(points1.keys(), points1.values())
    plt.title("Single Slit") 
    
    plt.subplot(222)
    plt.scatter(points2.keys(), points2.values())
    plt.title("Double Slit") 
    
    plt.subplot(223)
    plt.scatter(pointsN.keys(), pointsN.values())
    plt.title("N-Slit") 
    
    plt.subplot(224)
    plt.scatter(pointsSq.keys(), pointsSq.values())
    plt.title("Square Slit") 
    
    plt.show()    