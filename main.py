#run from here
#because this is main

import intensity_calculator as ic
import buckets as B
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
import square_intensity as sq
import triangle_intensity as tr
#import circular_intensity as cc
import step_func as sf

def run(command):
    if(command == "single"): 
        a = input("enter a slit width (microns): ")
        a = float(a) * (1e-6)
        D = input("enter a distance from the screen (m): ")
        D = float(D)   
    elif(command == "double"): 
        a = input("enter a slit separation (microns): ") #for double slit
        a = float(a) * (1e-6)
        D = input("enter a distance from the screen (m): ")
        D = float(D)
    elif(command == "N"):
        a = input("enter a slit separation (1e-10 m): ")
        a = float(a) * (1e-10)        
        D = input("enter a distance from the screen (m): ")
        D = float(D)
        n = input("enter number of slits: ")             
        n = int(n)
    elif(command == "square"):
        a = input("enter a side length (microns): ")
        a = float(a) * (1e-6)        
        D = input("enter a distance from the screen (m): ")
        D = float(D)   
    elif(command == "triangle"):
        a = input("enter height of triangle (microns): ")
        a = float(a) * (10e-6)        
        D = input("enter a distance from the screen (m): ")
        D = float(D)         
    #circle not included as an elif statement because it only needs wavelength paramter (like all others)
    else:
        print("Command not understood. Try again.")
        return False

    plt.figure(figsize = (10,5), tight_layout = True)

    #user inputs needed for any of the types of slit experiments
    l = input("enter a wavelength (nm): ")
    l = float(l) * (10e-9)    
    num = input("input the number of particles: ")
    num = int(num)

    #calculating the overall intensity distribution
    if(command == "single"):
        values = ic.single_intensity(a,l,D)
    elif(command == "double"):
        values = ic.double_intensity(a, l, D)
    elif(command == "N"):
        values = ic.n_intensity(n,a,l,D)
    #elif(command == "circle"):
    #    values = cc.circular_intensity(l)
    elif(command == "square"):
        values = sq.square_intensity(a,l,D)
    elif(command == "triangle"):
        values = tr.triangle_intensity(a,l,D)
                        
    intensity = values[1]   #entire intensity distribution
    x_vals = values[0]      #set of all x values for the distribution
    
    #determining where the particle should go
    x = list()
    for i in range(0, num):
        bucket_info = B.bucket(intensity, x_vals)
        intensity1 = bucket_info[1]     #these are named 1 so intensity and x_vals don't get overwritten
        x_vals1 = bucket_info[0]
        while( len(x_vals1) > 1 ):      #break buckets into buckets until only 1 thing in it
            bucket_info = B.bucket(intensity1, x_vals1)
            intensity1 = bucket_info[1]
            x_vals1 = bucket_info[0]
        if random.randint(0,10)%2 == 0: #because for some reason otherwise they're only negative
            x.append(x_vals1[0])
        else:
            x.append(-1*x_vals1[0])
    
    #make a histogram based on how many particles end up at each x value
    points = dict()
    for i in x:
        if i in points:
            points[i] += 1
        else:
            points[i] = 1   
    
    T = list()
    for i in points.keys():
        T.append(points[i])
    
    #feelin' plot plot plot
    plt.subplot(122)
    plt.scatter(points.keys(), points.values(), c=T)
    plt.title("Experimental, {} particles".format(num)) 
    plt.axis([-20,20,0,max(points.values())])
    plt.show()    
            
    return True


"""
Actual main code starts here:
"""

#opening message
print("Running options: single (Single Slit), double (Double Slit), N (N Slits),",
      "circle (Circular Aperture), square (Square Aperture), triangle (Triangle Aperture).\n",
      "Enter 'step' to run the step by step simulation. Enter 'stop' to end.")
command = input("Enter command: ")

while(command != "stop"):
    
    if(command == "step"):
        sf.step()
    
    else:
        run(command)
    
    command = input("Enter a command: ")