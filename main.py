#run from here
#because this is main

import intensity_calculator as ic
import buckets as B
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
from test import bucket_run

plt.figure(figsize = (10,5), tight_layout = True)

#user inputs
l = input("enter a wavelength (nm): ")
l = float(l) * (10**-9)
a = input("enter a slit width (micro m): ")      #for single slit
a = float(a) * (10**-6)
d = input("enter a slit separation (micro m): ") #for double slit
d = float(d) * (10**-10)
D = input("enter a distance from the screen (m): ")
D = float(D)
n = input("enter number of slits: ")             #for n slit
n = int(n)
num = input("finally, input the number of particles: ")
num = int(num)

#calculating the overall intensity distribution
values = ic.double_intensity(a, l, D)
##values = ic.n_intensity(n, d, l, D)
intensity = values[1]   #entire intensity distribution
x_vals = values[0]      #set of all x values for the distribution

#determining where the particle should go
x = list()
for i in range(0, num):
    bucket_info = B.bucket(intensity, x_vals)
    ##bucket_info = bucket_run(intensity, x_vals) #break entire intensity into buckets
    intensity1 = bucket_info[0]     #these are named 1 so intensity and x_vals don't get overwritten
    x_vals1 = bucket_info[1]
    while( len(x_vals1) > 1 ):      #break buckets into buckets until only 1 thing in it
        ##bucket_info = bucket_run(intensity1, x_vals1)
        bucket_info = B.bucket(intensity, x_vals)
        intensity1 = bucket_info[0]
        x_vals1 = bucket_info[1]
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

#feelin' plot plot plot
plt.subplot(122)
plt.bar(points.keys(), points.values())
plt.title("Experimental, {} particles".format(num)) 
plt.axis([-n,n,0,max(points.values())])
plt.show()