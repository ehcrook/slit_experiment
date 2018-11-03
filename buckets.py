import numpy as np
import matplotlib.pyplot as plt
import math as math
import random

def bucket(I, y):
    #calculating the probabilities for each point in the distribution
    s = 0
    for val in I:
        s = s+val
        
    probabilities = list()
    for val in I:
        probabilities.append((val/s)*100)
        
    #print(probabilities)
    
    #making probability buckets
    buckets = list()
    current_bucket = list()
    current_sum = 0
    
    x = 0
    while x < len(probabilities):
        prob = probabilities[x]
        current_bucket.append(y[x])
        current_sum = current_sum + prob
        if (math.floor(current_sum) == 1) or (1-current_sum < 0.01):
            buckets.append(current_bucket)
            current_sum = 0
            current_bucket = list()
        x = x+1
    
    #selecting a bucket
    bucket = buckets[ random.randint(0,len(buckets)) ]
    return bucket