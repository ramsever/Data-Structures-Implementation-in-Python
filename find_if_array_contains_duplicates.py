##################################################
#
# find if array contains duplicated.py
#
# using python dictionary as a hash table
#
##################################################
import sys

def find_if_array_contain_duplicates(array):

    d = dict()
    for e in array:
        if e in d.keys():
            print('dumplication has been found')
            return
        d[e] = 1
    print('no dumplication was found')
        
def main():

    array = sys.argv[1]
    find_if_array_contain_duplicates(array)

if __name__ == '__main__':
    main()
