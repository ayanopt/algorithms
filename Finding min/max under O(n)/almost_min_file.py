import math
def almost_min(list_in):
    list_size = len(list_in)
    root_size = math.log(list_size)
    my_min = list_in[0]
    for i in range(2,int(root_size)+1):
        j = 1
        while j < list_size:
            my_min = min(list_in[j],my_min)
            j = j*i
    return my_min
    