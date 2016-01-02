import math

##################################################################
#
# Newton Approximation for SQRT and SQRT
#
# Author: Ram Sever
#
# Links:
# Methods of computing square roots:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots 
# Newton's method:
# https://en.wikipedia.org/wiki/Newton%27s_method
#
##################################################################


def f_sqr(s):
    # initial guess
    x = 1
    for k in range(100):
        x = 2 * math.sqrt(x) * s - x
    return x
    
def f_sqrt(s):
    # initial guess
    x = 1
    for k in range(100):
        x = 0.5*(x+s/x)
    return x

    
def main():
    
    s = 2
    print('{0}^2   = {1}'.format(s,f_sqr(s)))
    print('{0}^0.5 = {1}'.format(s,f_sqrt(s)))
    

if __name__ == '__main__':
    main()
    
