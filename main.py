#run from here
#because this is main

import intensity_calculator as ic
import buckets

l = input("enter a wavelength (nm): ")
l = float(l) * (10**-9)
a = input("enter a slit width (micro m): ")
a = float(a) * (10**-6) 
D = input("enter a distance from the screen (m): ")
D = float(D)
n = input("enter a counting number: ")
n = int(n)

values = ic.single_intensity(n, a, l, D)
intensity = values[1]
x_vals = values[0]

bucket = buckets.bucket(intensity, x_vals)
print(bucket)