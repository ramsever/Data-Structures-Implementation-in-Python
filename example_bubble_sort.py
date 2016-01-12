import numpy as np

##################################################################
#
# Bubble Sort
#
# Author: Ram Sever
#
# Links:
# https://en.wikipedia.org/wiki/Bubble_sort
#
##################################################################

def bubble_sort(a,direction):
    for k1 in range(0,len(a),1):
        for k2 in range(0,len(a)-k1-1,1):
            if (direction == 'up'):
                if (a[k2] > a[k2+1]):
                    # swap
                    a[k2] , a[k2+1] = a[k2+1] , a[k2]
            else:
                if (a[k2] < a[k2+1]):
                    # swap
                    a[k2] , a[k2+1] = a[k2+1] , a[k2]
    return a
    
def main():

    a = list(np.random.permutation(10))
    print('array before sorting = {0}'.format(a))
    b = bubble_sort(a,'up')
    print('array after sorting up = {0}'.format(b))
    b = bubble_sort(a,'down')
    print('array after sorting down = {0}'.format(b))

if __name__ == '__main__':
    main()