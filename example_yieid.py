##################################################
#
# Example Usage of Yield
#
##################################################
import sys  
import ipdb

def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n * fib(n-1)

def number_generator(k):
    v = range(k)
    for n in v:
        yield fib(n)
    

def main():
    #ipdb.set_trace()
    if len(sys.argv)==1:
        m = 5
    else:
        try:
            m = int(sys.argv[1])
        except:
            # default value
            m = 5
        
    for k,n in enumerate(number_generator(m)):
        print('Fib({0})={1}'.format(k,n))

if __name__ == '__main__':
    main()
