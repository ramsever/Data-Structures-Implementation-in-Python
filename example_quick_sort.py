##################################################
#
# QuickSort implementation
#
##################################################

import numpy as np
import ipdb

# enable debug
enable_debug = 0

def partition(array,p,q):
    r = q
    direction = 0 # move p to the right
    while (p<q):
        if (direction==0):
            if (array[r]>=array[p]):
                p += 1
            else:
                #swap
                array[r],array[p] = array[p],array[r]
                r = p
                direction = 1
                continue
        if (direction == 1):
            if (array[r] <= array[q]):
                q -= 1
            else:
                # swap
                array[r],array[q] = array[q],array[r]
                r = q
                direction = 0
                continue
    return array,r

def quick_sort(array,p,q):
    if (p>=q):
        return array
    array,r = partition(array,p,q)
    if (enable_debug==1):
        print array,p,q,r
        print "(p,r-1) = " , p , r-1
    array = quick_sort(array,p,r-1)
    if (enable_debug==1):
        print array
        print "(r+1,q) = " , r+1 , q
    array = quick_sort(array,r+1,q)
    if (enable_debug==1):
        print array
    return array
    

def main():
    array = list(np.random.permutation(10))
    
    # using python built-in library for sorting
    sorted_array = sorted(array,key = lambda x:x,reverse=False)
    
    # our implementation of quick sort
    quicksort_array = quick_sort(array,0,len(array)-1)
    
    print('array       = {0}'.format(array))
    print('python sort = {0}'.format(sorted_array))
    print('quicksort   = {0}'.format(quicksort_array))

if __name__ == '__main__':
    main()









