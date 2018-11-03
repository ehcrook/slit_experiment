import numpy as np
import math as math
import random
from datetime import datetime

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
    bucket_intensity = list()
    current_bucket = list()
    current_intensity = list()
    current_sum = 0
    
    x = 0
    while x < len(probabilities):
        prob = probabilities[x]
        current_bucket.append(y[x])
        current_intensity.append(I[x])
        current_sum = current_sum + prob
        if (math.floor(current_sum) == 1) or (1-current_sum < 0.01):
            buckets.append(current_bucket)
            bucket_intensity.append(current_intensity)
            current_sum = 0
            current_bucket = list()
            current_intensity = list()
        x = x+1
        
    # print( "length of buckets: ", len(buckets) )
    
    #selecting a bucket
    random.seed(datetime.now())
    num = random.randint(0,len(buckets))
    if(num == len(buckets)):
        num = 0
    # print(num)
    bucket = buckets[num]
    intensity = bucket_intensity[num]
    # print( "length of bucket: ", len(bucket) )
    return [bucket, intensity]