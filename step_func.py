#code for the step functionality
#showing the particles being added one by one
#basically a simulation of the slit experiment

import intensity_calculator as ic
import square_intensity as sq
import matplotlib.pyplot as plt
import numpy as np
import buckets as B
import random
from datetime import datetime

def make_dict(x):
    points = dict()
    for i in x:
        if i in points:
            points[i] += 1
        else:
            points[i] = 1
    return points
        
def step():
    a = 6e-6
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
    
        for i in range(0, num):
            bucket_info = B.bucket(intensity1, x_vals1)
            intensity11 = bucket_info[1]
            x_vals11 = bucket_info[0]
            while( len(x_vals11) > 1 ):   
                bucket_info = B.bucket(intensity11, x_vals11)
                intensity11 = bucket_info[1]
                x_vals11 = bucket_info[0]
            if random.randint(0,10)%2 == 0:
                x1.append(x_vals11[0])
            else:
                x1.append(-1*x_vals11[0])       
        
        for i in range(0, num):
            bucket_info = B.bucket(intensity2, x_vals2)
            intensity12 = bucket_info[1]
            x_vals12 = bucket_info[0]
            while( len(x_vals12) > 1 ):   
                bucket_info = B.bucket(intensity12, x_vals12)
                intensity12 = bucket_info[1]
                x_vals12 = bucket_info[0]
            if random.randint(0,10)%2 == 0:
                x2.append(x_vals12[0])
            else:
                x2.append(-1*x_vals12[0])
                
        for i in range(0, num):
            bucket_info = B.bucket(intensityN, x_valsN)
            intensity1N = bucket_info[1]
            x_vals1N = bucket_info[0]
            while( len(x_vals1N) > 1 ):   
                bucket_info = B.bucket(intensity1N, x_vals1N)
                intensity1N = bucket_info[1]
                x_vals1N = bucket_info[0]
            if random.randint(0,10)%2 == 0:
                xN.append(x_vals1N[0])
            else:
                xN.append(-1*x_vals1N[0])   
                
        for i in range(0, num):
            bucket_info = B.bucket(intensitySq, x_valsSq)
            intensity1Sq = bucket_info[1]
            x_vals1Sq = bucket_info[0]
            while( len(x_vals1Sq) > 1 ):   
                bucket_info = B.bucket(intensity1Sq, x_vals1Sq)
                intensity1Sq = bucket_info[1]
                x_vals1Sq = bucket_info[0]
            if random.randint(0,10)%2 == 0:
                xSq.append(x_vals1Sq[0])
            else:
                xSq.append(-1*x_vals1Sq[0])       
        
        points1 = make_dict(x1)
        points2 = make_dict(x2)
        pointsN = make_dict(xN)
        pointsSq = make_dict(xSq)
        
        T = list()
        for i in points1.keys():
            T.append(points1[i])        
            
        plt.subplot(221)
        plt.scatter(points1.keys(), points1.values(), c=T)
        plt.title("Single Slit") 
        
        T = list()
        for i in points2.keys():
            T.append(points2[i])        
        
        plt.subplot(222)
        plt.scatter(points2.keys(), points2.values(), c=T)
        plt.title("Double Slit") 
        
        T = list()
        for i in pointsN.keys():
            T.append(pointsN[i])        
        
        plt.subplot(223)
        plt.scatter(pointsN.keys(), pointsN.values(), c=T)
        plt.title("N-Slit") 
        
        T = list()
        for i in pointsSq.keys():
            T.append(pointsSq[i])        
        
        plt.subplot(224)
        plt.scatter(pointsSq.keys(), pointsSq.values(), c=T)
        plt.title("Square Slit") 
        
        plt.show()    