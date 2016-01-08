##################################################
#
# Insertion Sort implementation
#
##################################################

import numpy as np
import ipdb

# enable debug
enable_debug = 0

def insertion_sort(a):
    for i in range(1,len(a),1):
        j = i
        while ((j>0) and (a[j-1]>a[j])):
            print a
            a[j-1],a[j] = a[j],a[j-1]
            j = j - 1
    return a

def main():
    array = list(np.random.permutation(10))
    print array
    
    # using python built-in library for sorting
    sorted_array = sorted(array,key = lambda x:x,reverse=False)
    
    # our implementation of quick sort
    insertion_sort_array = insertion_sort(array)
    
    print('array       = {0}'.format(array))
    print('python sort = {0}'.format(sorted_array))
    print('insertion sort   = {0}'.format(insertion_sort_array))

if __name__ == '__main__':
    main()









