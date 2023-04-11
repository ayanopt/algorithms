import math
import random
def almost_min(list_in):
    list_size = len(list_in)
    root_size = math.sqrt(list_size)
    my_min = list_in[0]
    for i in range(2,int(root_size)+1):
        # Half of the time, I will traverse either left to right or right to left
        if i %2 == 0: 
            j = 1
            while j < list_size:
                # eps is a random term in between [j-i,j+i], it prevents repititions of the same values in the list
                eps = random.randint(max(0,j-i),min(list_size-1,j+i))
                my_min = min(list_in[eps],my_min)
                # exponential jumps with respect to i, each loop will hence have time complexity O(log_i(n))
                j = j*i
                
        else:
            j = -1
            while -j <= list_size:
                eps = random.randint(max(-list_size,j-i),min(-1,j+i))
                my_min = min(list_in[eps],my_min)
                j = j*i        
    return my_min
    