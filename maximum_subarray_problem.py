import ipdb
import numpy as np

#####################################################
#
# Maximum subarray problem
#
# Author: Ram Sever
#
#####################################################


# In computer science, the maximum subarray problem is the task of finding the contiguous subarray within 
# a one-dimensional array of numbers (containing at least one positive number) which has the largest sum. 
# For example, for the sequence of values -2, 1, -3, 4, -1, 2, 1, -5, 4; the contiguous subarray with the 
# largest sum is 4, -1, 2, 1, with sum 6.
# The problem was first posed by Ulf Grenander of Brown University in 1977, as a simplified model for maximum 
# likelihood estimation of patterns in digitized images. A linear time algorithm was found soon afterwards by 
# Jay Kadane of Carnegie-Mellon University (Bentley 1984).
#
# Link: https://en.wikipedia.org/wiki/Maximum_subarray_problem


def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# An alternative solution for the Maximum subarray problem
# which explicitly shows that if the intermediate sum receives
# a negative value it is set to None value
def max_subarray_alternative_solution(A):
    #ipdb.set_trace()
    max_so_far = None
    s = None
    for x in A:
        if s==None:
            if x>0:
                s = x
                if max_so_far == None:
                    max_so_far = s
                else:
                    max_so_far = max(max_so_far,s)
        else:
            if (s + x) > 0:
                s = s + x
                if max_so_far == None:
                    max_so_far = s
                else:
                    max_so_far = max(max_so_far,s)
            else:
                s = None
    return max_so_far
    
    
    
def main():
    # Generate a random vector of integers
    A = np.random.randint(-10,10,10)
    # Fixed Test cases:
    #A = [ -7, 8,   8,   8,   2,   5 , -7,   0, -10 , -6]
    print A
    print max_subarray(A)
    print max_subarray_alternative_solution(A)
    
if __name__ == '__main__':
    main()
    