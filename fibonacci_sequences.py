##################################################
#
# Fibonacci Sequences
#
# implement a function which returns the nth number 
# in Fibonacci sequences with an input n
#
# F(n) = F(n-1) + F(n-2)
#
##################################################
import sys

def fibonacci(n):
    if n < 1:
        return -1
    if n==1:    
        return 1
    if n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = int(sys.argv[1])
    print('Fib({0})={1}'.format(n,fibonacci(n)))
    
if __name__ == '__main__':
    main()
    
    
